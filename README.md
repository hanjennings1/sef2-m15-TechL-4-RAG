# RAG Helpdesk API

A small Flask API that answers support questions using retrieval-augmented generation (RAG). It matches an incoming question against a set of approved support documents, then (when there's a good enough match) passes that context to a local LLM served by [Ollama](https://ollama.com) to generate an answer.

## How it works

1. A question comes in through `POST /api/ask`.
2. The query is tokenized and compared against a small in-memory set of support documents (`documents.py`) using keyword matching, with common stopwords filtered out (`rag_service.py`).
3. If no relevant documents are found, the API returns a message saying there isn't enough information to answer — it does not fall back to a general-purpose LLM answer.
4. If matching documents are found, their content is used as context for the LLM (via `ai_client.py`, which talks to a local Ollama model) to generate a grounded answer.
5. The response includes the answer and the sources it was based on.

## Project structure

```
.
├── app.py              # Flask app factory and routes
├── ai_client.py         # Client for talking to the local Ollama model
├── documents.py         # In-memory store of approved support documents
├── rag_service.py       # Tokenizing, stopword filtering, and context retrieval
├── tests/                # Test suite
├── Pipfile               # Project dependencies
└── Pipfile.lock
```

## Requirements

- Python 3.12+
- [pipenv](https://pipenv.pypa.io/)
- [Ollama](https://ollama.com), running locally with a pulled model (e.g. `llama3.2`)

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/hanjennings1/sef2-m15-TechL-4-RAG.git
   cd sef2-m15-TechL-4-RAG
   ```

2. Install dependencies:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Make sure Ollama is running and the model is available:
   ```bash
   ollama pull llama3.2
   ```

## Running the app

```bash
flask --app app run --debug
```

The API will be available at `http://localhost:5000`.

## Endpoints

### `GET /api/health`

Simple health check.

**Response**
```json
{ "status": "ok" }
```

### `POST /api/ask`

Ask a support question.

**Request body**
```json
{ "query": "How do I reset my password?" }
```

**Response (match found)**
```json
{
  "query": "How do I reset my password?",
  "answer": "...",
  "sources": [ ... ]
}
```

**Response (no match found)**
```json
{
  "query": "...",
  "answer": "The approved support documents do not contain enough information to answer that question.",
  "sources": []
}
```

## Running tests

```bash
pipenv run pytest
```

## Notes

This project was built as part of a Flatiron School Software Engineering module (SEF2, Module 15) exploring retrieval-augmented generation with a local LLM.
