from sqlalchemy.orm import Session

from app.ingestion.loader import load_pdf

from app.ingestion.chunker import chunk_documents

from app.ingestion.embeddings import generate_embeddings

from app.db.models import Document, DocumentChunk

def ingest_document(

    filename: str,

    file_content: bytes,

    db: Session

):

    # Stage 1: Extract text

    pages = load_pdf(file_content)

    if not pages:

        raise ValueError("No extractable text found.")

    # Stage 2: Create chunks

    chunks = chunk_documents(pages)

    if not chunks:

        raise ValueError("No document chunks created.")

    # Stage 3: Generate embeddings

    vectors = generate_embeddings(chunks)

    if len(vectors) != len(chunks):

        raise RuntimeError("Embedding count mismatch.")

    try:

        # Stage 4: Create document record

        document = Document(filename=filename)

        db.add(document)

        db.flush()

        # Stage 5: Create chunk records

        records = []

        for chunk, vector in zip(chunks, vectors):

            record = DocumentChunk(

                document_id=document.id,

                content=chunk["content"],

                page_number=chunk["page_number"],

                chunk_index=chunk["chunk_index"],

                embedding=vector

            )

            records.append(record)

        db.add_all(records)

        result = {

            "document_id": document.id,

            "filename": filename,

            "chunks_created": len(records),

            "status": "completed"

        }

        # Stage 6: Persist everything

        db.commit()

        return result

    except Exception:

        db.rollback()

        raise