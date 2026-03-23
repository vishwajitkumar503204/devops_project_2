from sqlalchemy import Column, Integer, JSON, DateTime, String
from datetime import datetime
from app.db import Base  # ✅ FIX: Import from db.py, not models.py

class APIData(Base):
    __tablename__ = "api_data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    data = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<APIData(id={self.id}, created_at={self.created_at})>"