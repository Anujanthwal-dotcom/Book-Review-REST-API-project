from pydantic import BaseModel
from typing import Optional

class ReviewCreate(BaseModel):
    text: str
    rating: int
    book_id: int

class ReviewOut(BaseModel):
    id: int
    text: str
    rating: int
    user_id: int
    book_id: int

    class Config:
        from_attributes = True
