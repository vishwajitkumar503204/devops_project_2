from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from app.db import engine, Base
import threading
from app.worker import start_worker

app = FastAPI(
    title="DevOps Load Testing API",
    description="API for AWS Auto Scaling Load Testing",
    version="1.0.0"
)

# ✅ CORS Configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(router, prefix="/api", tags=["API"])

# Start worker in background
@app.on_event("startup")
def start_background_worker():
    print("🚀 Starting background worker...")
    thread = threading.Thread(target=start_worker, daemon=True)
    thread.start()

@app.on_event("shutdown")
def shutdown_event():
    print("🛑 Shutting down application...")

@app.get("/")
def root():
    return {
        "message": "DevOps Load Testing API",
        "status": "running",
        "endpoints": {
            "health": "/api/health",
            "data": "/api/data"
        }
    }