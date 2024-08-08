from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from final_setup.dependency import get_db
from ..service.main_service import MainService
from fastapi.templating import Jinja2Templates
from...model import models

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

@router.get("/safety_insights", response_class=HTMLResponse, )
async def safety_insights(request: Request, db:Session=Depends(get_db)):
    graph = await MainService.get_chloropleth_map(db)
    return templates.TemplateResponse("safety_insights.html", {"request": request, "plot":graph})

@router.get("/bicycle_routes", response_class=HTMLResponse)
async def bicycle_routes(request: Request):
    return templates.TemplateResponse("bicycle_routes.html", {"request": request})

@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@router.get("/lga")
async def get_lga(db:Session=Depends(get_db)):
    db_user = await MainService.get_lga(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user