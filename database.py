# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import config

DATABASE_URL = (
    f"mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}"
    f"@{config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DB}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

