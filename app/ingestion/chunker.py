from langchain_text_splitters import (

    RecursiveCharacterTextSplitter

)

from app.core.config import get_settings

settings = get_settings()

def chunk_documents(pages: list[dict]) -> list[dict]:

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=settings.CHUNK_SIZE,

        chunk_overlap=settings.CHUNK_OVERLAP

    )

    chunks = []

    for page in pages:

        texts = splitter.split_text(

            page["content"]

        )

        for text in texts:

            chunks.append({

                "content": text,

                "page_number": page["page_number"],

                "chunk_index": len(chunks)

            })

    return chunks