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

# @app.get("/", response_class=HTMLResponse)
# async def read_home(request: Request):
#     return templates.TemplateResponse("home.html", {"request": request})

# @app.get("/safety_insights", response_class=HTMLResponse)
# async def safety_insights(request: Request):
#     return templates.TemplateResponse("safety_insights.html", {"request": request})

# @app.get("/bicycle_routes", response_class=HTMLResponse)
# async def bicycle_routes(request: Request):
#     return templates.TemplateResponse("bicycle_routes.html", {"request": request})
