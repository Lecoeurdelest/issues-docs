import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Settings:

    LLM_API_KEY: str = os.getenv("LLM_API_KEY")

    LLM_MODEL: str = os.getenv("LLM_MODEL", "")
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "")

    DATA_DIR: str = os.getenv("DATA_DIR", "data")
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", 200))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", 0.0))
    TOP_K: int = int(os.getenv("TOP_K", 3))

    ELASTICSEARCH_URL: str = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
    ELASTICSEARCH_INDEX: str = os.getenv("ELASTICSEARCH_INDEX", "document_index")

    CHROMA_DB_PATH: str = os.getenv("CHROMA_DB_PATH", "db/chroma")
    CHROMA_COLLECTION_NAME: str = os.getenv("CHROMA_COLLECTION_NAME", "document_collection")

    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", 8080))

settings = Settings()

if not settings.LLM_API_KEY:
    raise ValueError("")

