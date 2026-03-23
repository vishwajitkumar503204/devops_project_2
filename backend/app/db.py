import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import Config

Base = declarative_base()

def get_engine():
    while True:
        try:
            engine = create_engine(Config.DB_URL)
            conn = engine.connect()
            conn.close()
            print("✅ Connected to DB")
            return engine
        except Exception as e:
            print("⏳ Waiting for DB...", e)
            time.sleep(2)

engine = get_engine()
SessionLocal = sessionmaker(bind=engine)