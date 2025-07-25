from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas import book as book_schema
from crud import book as book_crud
from db.deps import get_db
from api.deps import get_current_user
from models.user import User

router = APIRouter()

@router.post("/", response_model=book_schema.BookOut)
def create_book(
    book_in: book_schema.BookCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return book_crud.create_book(db=db, book=book_in, user_id=current_user.id)

@router.get("/", response_model=List[book_schema.BookOut])
def list_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return book_crud.get_books(db=db, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=book_schema.BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=book_schema.BookOut)
def update_book(
    book_id: int,
    book_in: book_schema.BookUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_book = book_crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    if db_book.created_by != current_user.id:
        raise HTTPException(status_code=403, detail="Not your book")
    return book_crud.update_book(db, db_book, book_in)

@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_book = book_crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    if db_book.created_by != current_user.id:
        raise HTTPException(status_code=403, detail="Not your book")
    book_crud.delete_book(db, db_book)
    return {"msg": "Book deleted"}
