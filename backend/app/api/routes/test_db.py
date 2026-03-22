from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db

router = APIRouter()


@router.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"status": "connected"}