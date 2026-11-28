from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str = "Agentic RAG API"

    DATABASE_URL: str

    OPENAI_API_KEY: str

    EMBEDDING_MODEL: str = "text-embedding-3-small"

    EMBEDDING_DIMENSIONS: int = 1536

    CHUNK_SIZE: int = 1000

    CHUNK_OVERLAP: int = 200

    model_config = SettingsConfigDict(

        env_file=".env",

        extra="ignore"

    )

@lru_cache

def get_settings() -> Settings:

    return Settings()  # type: ignore