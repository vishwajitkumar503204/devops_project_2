import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import Config

Base = declarative_base()

def get_engine():
    max_retries = 30
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            engine = create_engine(
                Config.DB_URL,
                pool_pre_ping=True,  # ✅ Auto-reconnect on connection loss
                pool_size=10,         # ✅ Connection pool for better performance
                max_overflow=20
            )
            conn = engine.connect()
            conn.close()
            print("✅ Connected to DB")
            return engine
        except Exception as e:
            retry_count += 1
            print(f"⏳ Waiting for DB (attempt {retry_count}/{max_retries})...", e)
            time.sleep(2)
    
    raise Exception("❌ Failed to connect to database after maximum retries")

engine = get_engine()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)