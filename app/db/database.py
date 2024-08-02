from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv



class Database:
    '''
    A static database connector class
    '''
    def __init__(self) -> None:
        '''
        Creating a database constructor
        '''
        load_dotenv()
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        self.DATABASE_NAME  = os.getenv("RDS_DATABASE_NAME")
        engine = create_engine(self.DATABASE_URL)
        self.base = declarative_base()
        self.sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    @staticmethod
    def get_db():
        '''
        Creating a get_db static method
        '''
        db = Database.sessionLocal()
        try:
            yield db
        finally:
            db.close()
