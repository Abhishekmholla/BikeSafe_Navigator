from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from ..setting import settings



database_connection_string = settings.database_connection_string
rds_database_name = settings.rds_database_name

engine = create_engine(database_connection_string + rds_database_name, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()




