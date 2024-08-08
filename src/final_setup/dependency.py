import pandas as pd
from .db.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def model_to_dataframe(model_query_result):
    
    # Extract column names from the model
    if not model_query_result:
        return pd.DataFrame() 

    columns = [column.name for column in model_query_result[0].__table__.columns]

    data = []
    for item in model_query_result:
        row = {col: getattr(item, col) for col in columns}
        data.append(row)

    df = pd.DataFrame(data, columns=columns)
    return df
