from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_connection_string: str = "mysql+pymysql://adminuser:adminuser123@bike-navigator-db.cd4q0qac8ce2.ap-southeast-2.rds.amazonaws.com:3306/"
    rds_database_name: str = "bike-navigator"


settings = Settings()