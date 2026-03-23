from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import Config

engine = create_engine(Config.DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()