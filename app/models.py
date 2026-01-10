from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from .database import Base

class Lineage(Base):
    __tablename__ = "lineage"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(String, index=True)
    source = Column(String)
    operation = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    extra_metadata = Column(JSON)
