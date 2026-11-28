from langchain_openai import OpenAIEmbeddings
from pydantic import SecretStr

from app.core.config import get_settings

settings = get_settings()

embedding_model = OpenAIEmbeddings(

    model=settings.EMBEDDING_MODEL,

    dimensions=settings.EMBEDDING_DIMENSIONS,

    api_key=SecretStr(settings.OPENAI_API_KEY)

)

def generate_embeddings(

    chunks: list[dict]

) -> list[list[float]]:

    texts = [

        chunk["content"]

        for chunk in chunks

    ]

    vectors = embedding_model.embed_documents(texts)

    return vectors