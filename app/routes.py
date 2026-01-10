from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from pydantic import BaseModel

from .database import SessionLocal
from .models import Lineage

router = APIRouter()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic request model
class LineageRequest(BaseModel):
    dataset_id: str
    source: str
    operation: str
    extra_metadata: dict

# POST: Log lineage
@router.post("/lineage/log")
def log_lineage(
    request: LineageRequest,
    db: Session = Depends(get_db)
):
    record = Lineage(
        dataset_id=request.dataset_id,
        source=request.source,
        operation=request.operation,
        timestamp=datetime.utcnow(),
        extra_metadata=request.extra_metadata
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return {"message": "Lineage logged successfully", "id": record.id}

# GET: Fetch lineage by dataset_id
@router.get("/lineage/{dataset_id}")
def get_lineage(dataset_id: str, db: Session = Depends(get_db)):
    return db.query(Lineage).filter(Lineage.dataset_id == dataset_id).all()
