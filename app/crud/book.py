from sqlalchemy.orm import Session
from models.book import Book
from schemas.book import BookCreate, BookUpdate

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: BookCreate, user_id: int):
    db_book = Book(**book.dict(), created_by=user_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, db_book: Book, book_update: BookUpdate):
    for field, value in book_update.dict(exclude_unset=True).items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, db_book: Book):
    db.delete(db_book)
    db.commit()
