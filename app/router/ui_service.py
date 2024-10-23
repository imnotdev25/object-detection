import httpx
from fastapi import File, UploadFile, Request, APIRouter
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

ui_router = APIRouter()
templates = Jinja2Templates(directory="templates")

@ui_router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})