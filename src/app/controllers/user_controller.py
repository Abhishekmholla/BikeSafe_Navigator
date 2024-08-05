from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.models import models
from .. import schemas
from ..dependency import get_db
from ..services.user_service import UserService


router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/{user_id}",response_model=schemas.User)
async def get_user(user_id:int, db:Session=Depends(get_db)):
    db_user = await UserService.get_user(db,user_id =user_id )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
    


# def get_user(db: Session, user_id: int):
#     return db.query(models.Users).filter(models.Users.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.Users).filter(models.Users.email == email).first()


# def get_users(db: Session, skip:int=0, limit:int=100):
#     # return db.query(models.User).offset(skip).limit(limit).all()
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user:schemas.UserCreate):
#     db_user = models.User(email=user.email,
#                           name=user.name)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_todos(db: Session, skip:int=0, limit: int=100):
#     return db.query(models.Todo).offset(skip).limit(limit).all()


# def create_user_todo(db:Session, todo:schemas.TodoCreate, user_id : int):
#     db_todo = models.Todo(**todo.model_dump(),owner_id=user_id )
#     db.add(db_todo)
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo


# NOTE :
# - add that instance object to your database session.
# - commit the changes to the database (so that they are saved).
# - refresh your instance (so that it contains any new data from the database, l