from fastapi import FastAPI
from app.routes import router
from app.db import engine, Base
import threading
from app.worker import start_worker

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(router)

# Start worker in background
@app.on_event("startup")
def start_background_worker():
    thread = threading.Thread(target=start_worker, daemon=True)
    thread.start()