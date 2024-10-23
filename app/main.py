import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.router.ai_service import ai_router
from app.router.ui_service import ui_router

app = FastAPI()
try: os.mkdir("static")
except: pass
app.mount("/static", StaticFiles(directory="static"), name="static")


UPLOAD_DIR = Path("static/uploads")
OUTPUT_DIR = Path("static/outputs")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ui_router)
app.include_router(ai_router)
