import os

from dotenv import load_dotenv

from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# Load environment variables from a .env file
load_dotenv()

# Database setup
engine = create_engine(f"postgresql://postgres:{os.getenv('POSTGRES_PASSWORD')}@db.bttijgbrforwaxpboawf.supabase.co:5432/postgres") #"password"
SessionLocal = sessionmaker(bind=engine)

# ORM Models
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))


# DB initialization
def init_db() -> None:
    Base.metadata.create_all(engine)


# Dependency to get DB session
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
    with SessionLocal() as session:
        
        # Create user
        user_new = User(name="Andy")
        session.add(user_new)
        session.commit()

        # Read users
        users = session.query(User).all()
        for user in users:
            print("--")
            print(type(user))
            print(user)
            print(user.name)
            print("--")