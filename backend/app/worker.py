import time
from app.db import SessionLocal
from app.models import Data

while True:
    try:
        db = SessionLocal()

        new_data = Data(value="Sample data")
        db.add(new_data)
        db.commit()

        print("Data saved")

    except Exception as e:
        print("Error:", e)

    finally:
        db.close()

    time.sleep(5)