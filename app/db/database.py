from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

DB_URL = os.getenv("DATABASE_URL")
RDS_Name = os.getenv("RDS_DATABASE_NAME")
engine = create_engine(DB_URL + RDS_Name, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

