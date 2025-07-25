from app.db.database import Base, engine
from app.models import user, book,review  # import other models later

def init_db():
    Base.metadata.create_all(bind=engine)
