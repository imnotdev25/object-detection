import base64
import io

from PIL import Image
from fastapi import APIRouter
from fastapi import File, UploadFile, HTTPException
from ultralytics import YOLO

from app.logger import logger

ai_router = APIRouter()

try:
    model = YOLO('models/yolov10s.pt')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@ai_router.get("/health")
async def health_check():
    """Check if the service and model are running properly"""
    return {"status": "healthy", "model_loaded": model is not None}

@ai_router.post("/detect")
async def detect_objects(file: UploadFile = File(...)):
    """
    Perform object detection on the uploaded image

    Returns:
        JSON with detections and output image base64 encoded
    """
    try:
        # Read image file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        image_extention = file.filename.split(".")[-1]
        image.save(f"static/uploads/{file.filename}")

        # Perform detection
        results = model(image)
        logger.info(f"Detected {len(results)} objects")


        if isinstance(results, list):
            logger.info("`results` is a list. Taking the first element.")
            results = results[0]
            img_path = results.save(f"static/outputs/{file.filename}")
            logger.info(f"Saved image to {img_path}")

        # Process results
        detections = []
        for idx, box in enumerate(results.boxes):
            # Extract bounding box coordinates
            x1, y1, x2, y2 = box.xyxy.cpu().numpy()[0]
            confidence = box.conf.cpu().numpy()[0]
            cls_id = int(box.cls.cpu().numpy()[0])
            class_name = results.names.get(cls_id, "unknown")

            detections.append({
                "xmin": float(x1),
                "ymin": float(y1),
                "xmax": float(x2),
                "ymax": float(y2),
                "confidence": float(confidence),
                "name": class_name
            })
        logger.info(f"Processed detections: \n {detections}")

        # Encode image to base64
        with open(f"{img_path}", "rb") as img_file:
            img_encoded = base64.b64encode(img_file.read()).decode('utf-8')
            img_file.close()


        return {
            "detections": detections,
            "image": f"data:image/{image_extention};base64,{img_encoded}"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e