from sqlalchemy.orm import Session
from ..db.models import models

class UserRepository:
    
    @staticmethod
    async def get_user(db: Session, user_id: int):
        return db.query(models.Users).filter(models.Users.id == user_id).first()