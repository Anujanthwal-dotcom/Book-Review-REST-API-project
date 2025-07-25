from fastapi import FastAPI
from api import auth,book,review

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(book.router, prefix="/books", tags=["books"])
app.include_router(review.router, prefix="/reviews", tags=["Reviews"])
@app.get("/")
def read_root():
    return {"msg": "BookStack API is running"}
