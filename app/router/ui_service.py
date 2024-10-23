from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates

ui_router = APIRouter()
templates = Jinja2Templates(directory="templates")

@ui_router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})