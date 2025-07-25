from sqlalchemy.orm import Session
from models.review import Review
from schemas.review import ReviewCreate

def create_review(db: Session, review_data: ReviewCreate, user_id: int):
    review = Review(**review_data.dict(), user_id=user_id)
    db.add(review)
    db.commit()
    db.refresh(review)
    return review

def get_reviews_for_book(db: Session, book_id: int):
    return db.query(Review).filter(Review.book_id == book_id).all()
