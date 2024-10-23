from dotenv import load_dotenv
from os import getenv

load_dotenv()

MODEL_PATH = getenv("MODEL_PATH", "app/models/yolov10s.pt")
UPLOAD_DIR = getenv("UPLOAD_DIR", "static/uploads")
OUTPUT_DIR = getenv("OUTPUT_DIR", "static/outputs")