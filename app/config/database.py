from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = "postgresql://Akshay:Akshay123@my-db-instance.cfpbahqjthxf.us-east-1.rds.amazonaws.com:5432/FirstTestDB"

engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
