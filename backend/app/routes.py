from fastapi import APIRouter
from app.db import SessionLocal
from app.models import APIData

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "OK"}

@router.get("/data")
def get_data():
    db = SessionLocal()
    results = db.query(APIData).order_by(APIData.created_at.desc()).limit(10).all()
    db.close()

    return [r.data for r in results]