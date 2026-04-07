# Legal AI

A legal API scaffold based on the health-api structure example, with Ollama-friendly architecture.

## Repository structure

- `legal-api/`
  - `src/`
    - `main.py` - FastAPI application entry point
    - `api/routes/` - route definitions and API endpoints
    - `core/` - application configuration and core logic
    - `workflows/` - workflow definitions for legal processes
    - `services/` - business service layer
    - `repositories/` - persistence and data access abstractions
    - `schemas/` - request/response models and validation
    - `db/` - database utilities and session management
    - `safety/` - safety checks, guardrails, and compliance logic
    - `prompts/` - Ollama prompt templates and legal reasoning helpers
    - `utils/` - general utility helpers
  - `tests/` - API and unit tests
  - `requirements.txt` - project dependencies
  - `Dockerfile` - containerization instructions
  - `.env.example` - environment variable template
  - `.gitignore` - files and folders to ignore

## Run locally

```bash
cd legal-api
python -m uvicorn src.main:app --reload
```
