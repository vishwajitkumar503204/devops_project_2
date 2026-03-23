from sqlalchemy import Column, Integer, JSON, DateTime
from datetime import datetime
from app.db import Base

class APIData(Base):
    __tablename__ = "api_data"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)