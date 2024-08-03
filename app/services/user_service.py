from sqlalchemy.orm import Session
from typing import List, Optional
from ..db.models import models
from ..schemas import Item

class ItemService:
    def get_item(self, db: Session, item_id: int) -> Optional[Item]:
        return db.query(models.Item).filter(models.Item.id == item_id).first()