# Legal AI

A legal API scaffold based on the Legal-AI for legal lawyer advice or giving the situation of the court sstay to make great advice how to give the article where and how to make decision and legal advice for individuals like maybe if needed to contact the lawyer.
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

