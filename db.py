import os
from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from models import Base

# Database setup
engine = create_engine(f"postgresql://postgres:{os.getenv('POSTGRES_PASSWORD')}@db.bttijgbrforwaxpboawf.supabase.co:5432/postgres")
SessionLocal = sessionmaker(bind=engine) 


#DB initialization
def init_db() -> None:
    Base.metadata.create_all(engine)