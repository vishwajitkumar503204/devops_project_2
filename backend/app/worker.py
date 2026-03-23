import time
import requests
from app.db import SessionLocal
from app.models import APIData
from app.config import Config

def start_worker():
    print("Worker started...")

    while True:
        try:
            response = requests.get(Config.API_URL, timeout=5)
            data = response.json()

            db = SessionLocal()

            record = APIData(data=data)
            db.add(record)
            db.commit()
            db.close()

            print("Data saved")

        except Exception as e:
            print("Error:", e)

        time.sleep(Config.POLL_INTERVAL)