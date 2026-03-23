import time
import requests
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from app.db import SessionLocal
from app.models import APIData
from app.config import Config

def fetch_and_store_data():
    """Fetch data from external API and store in database"""
    db = SessionLocal()
    try:
        # Fetch data from external API
        response = requests.get(Config.API_URL, timeout=10)
        response.raise_for_status()
        
        api_data = response.json()
        
        # Store in database
        new_record = APIData(data=api_data)
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        
        print(f"✅ Data saved at {datetime.utcnow()} - ID: {new_record.id}")
        return True
        
    except requests.RequestException as e:
        print(f"❌ API Request Error: {e}")
        db.rollback()
        return False
        
    except SQLAlchemyError as e:
        print(f"❌ Database Error: {e}")
        db.rollback()
        return False
        
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        db.rollback()
        return False
        
    finally:
        db.close()

def start_worker():
    """Background worker that polls API periodically"""
    print(f"🚀 Worker started - Polling every {Config.POLL_INTERVAL} seconds")
    
    while True:
        try:
            fetch_and_store_data()
        except Exception as e:
            print(f"❌ Worker error: {e}")
        
        time.sleep(Config.POLL_INTERVAL)