import os
from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# Database setup
engine = create_engine(f"postgresql://postgres:{os.getenv('POSTGRES_PASSWORD')}@db.bttijgbrforwaxpboawf.supabase.co:5432/postgres")
SessionLocal = sessionmaker(bind=engine) 

