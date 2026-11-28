from sqlalchemy import (

    Column,

    Integer,

    String,

    Text,

    ForeignKey,

    DateTime,

    func

)

from sqlalchemy.orm import declarative_base, relationship

from pgvector.sqlalchemy import Vector

from app.core.config import get_settings

settings = get_settings()

Base = declarative_base()

class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)

    filename = Column(String, nullable=False)

    created_at = Column(

        DateTime(timezone=True),

        server_default=func.now()

    )

    chunks = relationship(

        "DocumentChunk",

        back_populates="document",

        cascade="all, delete-orphan"

    )

class DocumentChunk(Base):

    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True)

    document_id = Column(

        Integer,

        ForeignKey("documents.id"),

        nullable=False

    )

    content = Column(Text, nullable=False)

    page_number = Column(Integer, nullable=False)

    chunk_index = Column(Integer, nullable=False)

    embedding = Column(

        Vector(settings.EMBEDDING_DIMENSIONS),

        nullable=False

    )

    document = relationship(

        "Document",

        back_populates="chunks"

    )