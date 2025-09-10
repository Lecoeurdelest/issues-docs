# Issues docs management and Assistant

This project builds an intelligent system to automatically generate Software Requirements Specification (SRS) documents from lightweight Use Cases (UC). The system then stores and allows users to query these documents in natural language via a RAG system.

## Core Idea

* **Lightweight SRS Generation**: Instead of a complex manual SRS writing process, the system allows users to provide lightweight Use Cases (simple, less detailed).
* **AI-Powered Generation**: Leverages large language models (LLMs) through **LangGraph** to automatically analyze, expand, and generate a complete structured SRS document.
* **Intelligent Storage**: Stores generated documents in **Elasticsearch**, a powerful search and analytics engine, while also creating vector embeddings stored in **ChromaDB** (or Elasticsearch) for semantic search.
* **Natural Language Querying**: Provides an API that enables users to “ask” about software requirements in natural language and receive accurate answers synthesized from the document repository.

## System Workflow

### 1. Document Generation Flow

1. **Input**: User sends a Use Case via the `/generate-srs` API.
2. **Parse**: **LangGraph** processes the input and uses a `docling` node to parse and extract UC into structured elements (actor, action, preconditions, postconditions...).
3. **Generate**: Structured data is passed through subsequent nodes in the graph. Each node is responsible for generating a specific section of the SRS (e.g., Overview, Functional Requirements, Non-functional Requirements, Event Flow\...) via LLM calls.
4. **Store**: The complete SRS document is stored in **Elasticsearch**.
5. **Index**: The document is chunked, embeddings are generated, and stored in **ChromaDB** for query readiness.

### 2. Query Flow (RAG)

1. **Query**: User sends a natural language question via the `/query-srs` API.
2. **Embed**: The system generates a vector embedding for the question.
3. **Retrieve**: Uses the question vector to find the most relevant document chunks from **ChromaDB**.
4. **Augment & Generate**: The original question and retrieved chunks are combined into a prompt and sent to an LLM, which synthesizes the final answer.

## Core Features

* **Non-IT Friendly Input**: Users provide only basic fields (title, actors, goal, main\_flow, outcome).
* **Automatic Versioning**: Versions auto-increment (1.0 for init, 1.1, 1.2… for updates).
* **Delta & Merge**: Updates stored as deltas; system auto-merges into latest version.
* **Full Audit Trail**: Keeps all history in `issues[]`, no deletion.
* **Raw Content Generation**: Builds plain text for embedding/RAG.
* **Query Support**: Natural language queries (simulate keyword search, future vector + LLM).
* **Rollback & Audit**: Retrieve history, compare versions, or rollback.

---

## Data Structure (Suggestion)

**UC Lightweight Document (after rephrasing in plain language)**

```json
{
  "id_uc": "UC-ORDER-001",
  "current_version": "1.1",
  "content": { ... },
  "issues": [ ... ]
}
```

**Issue**

```json
{
  "id_issue": "ISSUE-002",
  "type": "update",
  "version": "1.1",
  "content": { ... },
  "delta": { ... },
  "timestamp": "2025-09-11T09:00:00+07:00",
  "reporter": "Business Analyst"
}
```

---

## Usage Examples

**Create UC (init)**

```json
{
  "id_uc": "UC-LOGIN-001",
  "content": {
    "title": "User Login",
    "actors": ["User"],
    "goal": "Authenticate access",
    "main_flow": [
      "User enters username/password",
      "System verifies credentials",
      "System grants access"
    ],
    "outcome": "User successfully logs in"
  },
  "reporter": "BA",
  "timestamp": "2025-09-10T10:00:00+07:00"
}
```

**Update UC (delta)**

```json
{
  "id_uc": "UC-LOGIN-001",
  "delta": {
    "actors": ["User", "Authentication Service"],
    "main_flow[1]": "System validates via external auth service",
    "outcome": "Access granted with session token"
  },
  "reporter": "BA",
  "timestamp": "2025-09-11T11:00:00+07:00"
}
```

**Query**

* `"UC-ORDER-001 latest version?"`
* `"Show history of UC-ORDER-001"`
* `"Find UC related to payment"`

**Rollback / Compare**

* `"Rollback UC-ORDER-001 to version 1.0"`
* `"Compare version 1.0 and 1.1 of UC-ORDER-001"`

---

## Example Raw Content

```
Title: Quick Order
Actors: Customer, Payment System
Goal: Place an order with minimal steps
Main Flow:
- Customer clicks 'Buy Now'
- System shows payment form
- Customer selects Momo/ZaloPay
- System creates order
Outcome: Order created, confirmation sent
```


## Installation and Setup

### Requirements

* Docker and Docker Compose
* An API key from an LLM provider (e.g., OpenAI, Google AI)

### Steps

1. **Clone repository:**

   ```bash
   git clone https://github.com/Lecoeurdelest/issues-docs.git
   ```

2. **Configure environment variables:**
   Create a `.env` file in the root directory and add required details:

   ```env
   # Example  
        Elasticsearch
        ELASTICSEARCH_API_KEY=your_api_key
        ELASTIC_PASSWORD=elastic
        INDEX_NAME=use_cases

        # FastAPI
        API_HOST=0.0.0.0
        API_PORT=8008
        API_DEBUG=True

        # ChromaDB
        CHROMADB_HOST=0.0.0.0
        CHROMADB_PORT=8001
        CHROMADB_COLLECTION=uc_vectors
   ```

3. **Start background services:**

   ```bash
   docker-compose up -d
   ```

4. **Install Python dependencies:**

   ```bash
   conda create -n {your_env_name} python=3.11.13
   conda activate {your_env_name}
   pip install -r requirements.txt
   ```

5. **Run the FastAPI app:**

   ```bash
   cd src
   uvicorn main:app --reload --port 8008
   ```
