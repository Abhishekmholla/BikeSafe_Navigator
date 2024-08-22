import logging
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .db.database import engine
from .model import models
from .api.controller import main_controller

app = FastAPI()

app.mount("/static", StaticFiles(directory="final_setup/ui/static"), name="static")
templates = Jinja2Templates(directory="final_setup/ui/templates")
logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)
models.Base.metadata.create_all(bind = engine)

app.include_router(main_controller.router)
