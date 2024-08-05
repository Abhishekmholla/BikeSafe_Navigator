from fastapi import APIRouter, FastAPI, Depends, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .controllers import user_controller
from .db.models import models
from .db.database import engine
from .controllers import user_controller
from ..ui.main import app

models.Base.metadata.create_all(bind= engine)


app.include_router(user_controller.router)



