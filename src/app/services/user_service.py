from sqlalchemy.orm import Session
from typing import List, Optional
from ..db.models import models
from ..repository.user_repository import UserRepository

class UserService:
    
    @staticmethod
    async def get_user(db: Session, user_id: int):
        return await UserRepository.get_user(db, user_id)