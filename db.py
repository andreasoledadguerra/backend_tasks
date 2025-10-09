import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Database setup
engine = create_engine(f"postgresql://postgres:{os.getenv('POSTGRES_PASSWORD')}@db.bttijgbrforwaxpboawf.supabase.co:5432/postgres")
SessionLocal = sessionmaker(bind=engine) 


#DB initialization
def init_db() -> None:
    Base.metadata.create_all(engine)

# Dependency to get DB session
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()