from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.review import ReviewCreate, ReviewOut
from crud import review as crud_review
from db.deps import get_db
from api.deps import get_current_user
from models.user import User
from typing import List

router = APIRouter()

@router.post("/", response_model=ReviewOut)
def create_review(review: ReviewCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_review.create_review(db, review, current_user.id)

@router.get("/book/{book_id}", response_model=List[ReviewOut])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return crud_review.get_reviews_for_book(db, book_id)
