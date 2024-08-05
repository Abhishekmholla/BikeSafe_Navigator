from fastapi import APIRouter, FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.setting import Settings
from .controllers import user_controller
from .db.models import models
from . import schemas
from .db.database import engine
from dotenv import load_dotenv
from .controllers import user_controller


models.Base.metadata.create_all(bind= engine)

app = FastAPI()

app.include_router(user_controller.router)

app.mount("/static", StaticFiles(directory="src/ui/static"), name="static")
templates = Jinja2Templates(directory="src/ui/templates")

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/safety_insights", response_class=HTMLResponse)
async def safety_insights(request: Request):
    return templates.TemplateResponse("safety_insights.html", {"request": request})
