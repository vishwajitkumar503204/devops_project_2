from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from app.db import engine, Base
import threading
from app.worker import start_worker
from sqlalchemy import inspect

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

# ✅ Create tables safely (only if they don't exist)
def create_tables():
    """Create database tables if they don't exist"""
    try:
        inspector = inspect(engine)
        existing_tables = inspector.get_table_names()
        
        if 'api_data' not in existing_tables:
            Base.metadata.create_all(bind=engine)
            print("✅ Tables created successfully")
        else:
            print("ℹ️  Tables already exist, skipping creation")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

create_tables()

# Include routes
app.include_router(router, prefix="/api", tags=["API"])

# ✅ Start worker only once (not per worker process)
worker_started = False

@app.on_event("startup")
def start_background_worker():
    global worker_started
    
    # Only start worker once across all processes
    import os
    if os.getenv("WORKER_ENABLED", "true") == "true" and not worker_started:
        print("🚀 Starting background worker...")
        thread = threading.Thread(target=start_worker, daemon=True)
        thread.start()
        worker_started = True

@app.on_event("shutdown")
def shutdown_event():
    print("🛑 Shutting down application...")

@app.get("/")
def root():
    return {
        "message": "DevOps Load Testing API",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "health": "/api/health",
            "data": "/api/data",
            "docs": "/docs"
        }
    }