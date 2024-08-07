from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="",
    tags=["views"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
templates = Jinja2Templates(directory="final_setup/ui/templates")

@router.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/safety_insights", response_class=HTMLResponse)
async def safety_insights(request: Request):
    return templates.TemplateResponse("safety_insights.html", {"request": request})

@router.get("/bicycle_routes", response_class=HTMLResponse)
async def bicycle_routes(request: Request):
    return templates.TemplateResponse("bicycle_routes.html", {"request": request})
