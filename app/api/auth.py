from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin, UserOut
from db.deps import get_db
from crud import user as user_crud
from core.security import verify_password, create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    if user_crud.get_user_by_username(db, user_in.username):
        raise HTTPException(status_code=400, detail="Username already taken")
    if user_crud.get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already used")
    user = user_crud.create_user(db, user_in)
    return user

@router.post("/login")
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_username(db, user_in.username)
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer"}
