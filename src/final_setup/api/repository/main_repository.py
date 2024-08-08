from sqlalchemy.orm import Session

from final_setup.dependency import model_to_dataframe
from ...model import models

class MainRepository:
    
    @staticmethod
    async def get_lga(db: Session):
        return model_to_dataframe(db.query(models.Melbourne_LGA).all())
    
    @staticmethod
    async def get_accident_data(db:Session):
        return db.query(models.Accident.accident_no,models.Accident.lga_name).all()