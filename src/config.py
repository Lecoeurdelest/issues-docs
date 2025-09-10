from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra='ignore'
    )

    ELASTICSEARCH_URL: str = "http://localhost:9200"
    ELASTICSEARCH_API_KEY: str | None = None
    ELASTIC_PASSWORD: str | None = None
    INDEX_NAME: str = "use_cases"

    LLM_API_KEY: str | None = None
    LLM_MODEL: str | None = None
    EMBEDDING_MODEL: str | None = None
    EMBEDDING_DIM: int | None = None

    DOCLING_API_KEY: str | None = None
    DOCLING_OUTPUT_FORMAT: str | None = None

    CHROMADB_HOST: str = "0.0.0.0"
    CHROMADB_PORT: int = 8001
    CHROMADB_COLLECTION: str = "uc_vectors"

    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8008
    API_DEBUG: bool = False

    LANGCHAIN_TRACING: bool = False
    LANGCHAIN_PROJECT: str | None = None
    LANGGRAPH_MAX_STEPS: int = 10


settings = Settings()