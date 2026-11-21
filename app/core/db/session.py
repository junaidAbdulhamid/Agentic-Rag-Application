from sqlalchemy import create_engine, text

from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

settings = get_settings()

engine = create_engine(

    settings.DATABASE_URL,

    pool_pre_ping=True

)

SessionLocal = sessionmaker(

    bind=engine,

    autoflush=False

)

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()

def check_database_connection():

    with engine.connect() as connection:

        result = connection.execute(text("SELECT 1"))

        return result.scalar() == 1