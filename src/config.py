import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv(override=True)

class Settings:
    ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
    ELASTICSEARCH_API_KEY = os.getenv("ELASTICSEARCH_API_KEY")
    INDEX_NAME = os.getenv("INDEX_NAME", "use_cases")

    LLM_API_KEY = None
    LLM_MODEL = None
    EMBEDDING_MODEL = None
    EMBEDDING_DIM = None
    DOCLING_API_KEY = None
    DOCLING_OUTPUT_FORMAT = None
    CHROMADB_HOST = None
    CHROMADB_PORT = None
    CHROMADB_COLLECTION = None

    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", 8000))
    API_DEBUG = os.getenv("API_DEBUG", "False").lower() == "true"

    LANGCHAIN_TRACING = None
    LANGCHAIN_PROJECT = None
    LANGGRAPH_MAX_STEPS = None

    def validate(self):
        pass

settings = Settings()
settings.validate()

es_client = Elasticsearch(
    hosts=[settings.ELASTICSEARCH_URL],
    api_key=settings.ELASTICSEARCH_API_KEY
)