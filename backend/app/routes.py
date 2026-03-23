from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from app.db import SessionLocal
from app.models import APIData

router = APIRouter()

@router.get("/health")
def health():
    """Health check endpoint"""
    try:
        db = SessionLocal()
        # Test DB connection
        db.execute("SELECT 1")
        db.close()
        return {"status": "OK", "database": "connected"}
    except Exception as e:
        return {"status": "DEGRADED", "database": "disconnected", "error": str(e)}

@router.get("/data")
def get_data():
    """Fetch latest 10 records from database"""
    db = SessionLocal()
    try:
        results = db.query(APIData).order_by(APIData.created_at.desc()).limit(10).all()
        return [{"id": r.id, "data": r.data, "created_at": r.created_at.isoformat()} for r in results]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        db.close()