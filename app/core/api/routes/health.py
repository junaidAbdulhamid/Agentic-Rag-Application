from fastapi import APIRouter, HTTPException, status

from app.core.db.session import check_database_connection


router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
def health_check():
    try:
        if not check_database_connection():
            raise RuntimeError("Database check failed")
        return {"status": "healthy", "database": "connected"}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unavailable",
        ) from None
