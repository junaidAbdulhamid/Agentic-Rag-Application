import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.db.session import engine  # pyright: ignore[reportMissingImports]

from app.db.models import Base  # pyright: ignore[reportMissingImports]

def init_db():

    Base.metadata.create_all(bind=engine)

    print("Database tables created successfully.")

if __name__ == "__main__":

    init_db()