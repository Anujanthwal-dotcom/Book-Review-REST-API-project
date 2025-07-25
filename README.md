# 📚 BookStack – FastAPI Book Review API

BookStack is a backend API service built using FastAPI and MySQL that allows users to register, log in, add books, and post reviews. It's structured, scalable, and follows modern Python development practices including JWT-based authentication and modular architecture.

## 🚀 Features

- ✅ User Registration and Login with JWT Authentication
- 📚 CRUD APIs for Books and Reviews
- 🔒 Secure password hashing using Passlib
- 🧱 MySQL with SQLAlchemy ORM
- 🔧 FastAPI's interactive Swagger UI
- 🧪 Modular and maintainable codebase

## 🛠 Tech Stack

- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- Passlib
- JWT (python-jose)
- Uvicorn

## 📁 Project Structure

```
app/
├── api/
│   └── v1/
│       ├── auth.py
│       ├── books.py
│       └── reviews.py
├── core/
│   └── config.py
├── db/
│   ├── database.py
│   └── init_db.py
├── models/
│   ├── user.py
│   ├── book.py
│   └── review.py
├── schemas/
│   ├── user.py
│   ├── book.py
│   └── review.py
├── main.py
.env
requirements.txt
README.md
```

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/bookstack.git
cd bookstack
```

### 2. Create a virtual environment

```bash
python -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

Create a `.env` file in the root with the following:

```env
DATABASE_URL=mysql+mysqlconnector://root:yourpassword@localhost:3306/bookstack
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Create MySQL database

```sql
CREATE DATABASE bookstack;
```

### 6. Initialize the database

```bash
python -c "from app.db.init_db import init_db; init_db()"
```

### 7. Run the server

```bash
uvicorn app.main:app --reload
```

Access:
- Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🧪 API Usage

### 🔐 Authentication

#### Register

`POST /auth/register`

```json
{
  "email": "user@example.com",
  "password": "strongpassword"
}
```

#### Login

`POST /auth/login`

```json
{
  "email": "user@example.com",
  "password": "strongpassword"
}
```

Returns JWT access token. Use it in headers:

```
Authorization: Bearer <your_token>
```

### 📚 Book Endpoints

#### Add Book

`POST /books`

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "description": "A book about habits."
}
```

#### Get All Books

`GET /books`

#### Get Book by ID

`GET /books/{book_id}`

### ✍️ Review Endpoints

#### Add Review

`POST /reviews`

```json
{
  "book_id": 1,
  "rating": 5,
  "review": "Fantastic read!"
}
```

#### Get Reviews for Book

`GET /reviews/book/{book_id}`

## 📌 Example cURL Commands

```bash
curl -X POST http://127.0.0.1:8000/auth/register \
-H "Content-Type: application/json" \
-d '{"email":"test@example.com","password":"123456"}'
```

```bash
curl -X POST http://127.0.0.1:8000/auth/login \
-H "Content-Type: application/json" \
-d '{"email":"test@example.com","password":"123456"}'
```

## 🛠 Common Issues

**bcrypt error:**

If you encounter:

```
AttributeError: module 'bcrypt' has no attribute '__about__'
```

Fix it with:

```bash
pip uninstall bcrypt
pip install bcrypt==4.0.1
```

**Pydantic v2 Compatibility:**

If you face issues with `BaseSettings`, install:

```bash
pip install pydantic-settings
```

And update configs using `from pydantic_settings import BaseSettings`.

## 🧱 Future Improvements

- ✅ Docker Support
- ✅ Alembic for migrations
- ✅ Pagination & Filtering
- ✅ Role-based permissions
- ✅ CI/CD Integration

## 📄 License

MIT License

---

Made with ❤️ by [Anuj]
