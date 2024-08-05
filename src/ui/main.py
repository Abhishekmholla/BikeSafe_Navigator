import logging
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="ui/static"), name="static")
templates = Jinja2Templates(directory="ui/templates")
logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/safety_insights", response_class=HTMLResponse)
async def safety_insights(request: Request):
    return templates.TemplateResponse("safety_insights.html", {"request": request})

@app.get("/bicycle_routes", response_class=HTMLResponse)
async def bicycle_routes(request: Request):
    print("Abhis")
    return templates.TemplateResponse("bicycle_routes.html", {"request": request})
