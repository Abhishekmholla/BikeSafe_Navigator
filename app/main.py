from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .controllers import user_controller
from .db.models import models
from . import schemas
from .db.database import engine
from dotenv import load_dotenv
from .controllers import user_controller

load_dotenv()
models.Base.metadata.create_all(bind= engine)

app = FastAPI()

app.include_router(user_controller.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/safety_insights", response_class=HTMLResponse)
async def safety_insights(request: Request):
    return templates.TemplateResponse("safety_insights.html", {"request": request})

# @app.post("/users/",response_model=schemas.User)
# def post_user(user:schemas.UserCreate, db:Session=Depends(get_db)):
#     db_user = user_controller.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return user_controller.create_user(db=db,user=user)


# @app.get("/users/", response_model=list[schemas.User])
# def get_users(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
#     users = user_controller.get_users(db,skip=skip,limit=limit)
#     return users


# @app.get("/users/{user_id}/",response_model=schemas.User)
# def get_user(user_id:int, db:Session=Depends(get_db)):
#     db_user = user_controller.get_user(db,user_id =user_id )
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/todos/",response_model=schemas.Todo)
# def post_todo_for_user(user_id:int, todo:schemas.TodoCreate, db:Session=Depends(get_db)):
#     return user_controller.create_user_todo(db=db,user_id=user_id, todo=todo)


# @app.get("/todos/", response_model=list[schemas.Todo])
# def get_todos(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
#     todos = user_controller.get_todos(db,skip=skip,limit=limit)
#     return todos
