## Object Detection with YOLOv10

### Introduction
This project is a simple implementation of object detection using YOLOv10. The model is trained on the COCO dataset and can detect 80 different classes of objects. The model is trained on a custom dataset and can be used to detect objects in images


### Requirements
- Python 3.11
- torch[cpu]
- torchvision
- numpy
- ultralytics/yolov10s

### Setup
1. Clone the repository
2. Run Docker container
    ```bash
    docker build -t yolo-v10-detection .
    docker run -it --rm --name yolo-v10-detection yolo-v10-detection
    ```
3. Visit localhost:8000 to access ui

### Approach
- The model is trained on the COCO dataset, used pretrained weights from the ultralytics/yolov10s repository