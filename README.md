# GraphRAG Development Environment

Graph-based Retrieval Augmented Generation (RAG) system using LangChain, LlamaIndex, Neo4j, and FAISS.

## Quick Start

```bash
# Install dependencies
poetry install --no-root

# Register Jupyter kernel
poetry run python -m ipykernel install --user --name graphrag --display-name "Python (graphrag)"

# Start Neo4j database
docker compose up -d

# Verify Neo4j connection
poetry run python src/neo4j_client.py

# Launch Jupyter Lab
poetry run jupyter lab

# Stop Neo4j when done
docker compose down
```

## Project Structure

```
graphrag/
├── notebooks/           # Jupyter notebooks
├── src/                # Source code modules
│   └── neo4j_client.py # Neo4j connectivity
├── tests/              # Unit tests
├── data/
│   ├── raw/           # Raw data files
│   └── processed/     # Processed data files
├── models/            # Saved models
├── neo4j/
│   ├── data/         # Neo4j database files
│   └── logs/         # Neo4j logs
├── docker-compose.yml # Neo4j service definition
├── .env.sample       # Environment variables template
└── pyproject.toml    # Poetry configuration
```

## Stack

### Core Framework
- **LangChain** (^0.2.0) - LLM application framework
- **LangChain Community** (^0.2.0) - Community integrations
- **LangChain Ollama** (^0.3.8) - Ollama LLM integration
- **LlamaIndex** (^0.14.0) - Data framework for LLM apps

### Graph Database
- **Neo4j** (^6.0.0) - Graph database driver
- **Docker Compose** - Neo4j service (ports 7474/7687)

### Vector Search & Embeddings
- **FAISS CPU** (^1.13.0) - Vector similarity search
- **Sentence Transformers** (^2.7.0) - Embedding models

### Data & ML
- **pandas** (^2.2.2), **numpy** (^2.0.0)
- **scikit-learn** (^1.5.0)

### App & Utilities
- **Streamlit** (^1.31.0) - Web app framework
- **OpenAI** (^1.0.0) - OpenAI API client
- **TikToken** (^0.7.0) - Token counting
- **NetworkX** (^3.0) - Graph algorithms
- **Unstructured** (^0.14.0) - Document parsing

### Development
- **JupyterLab** (^4.0.0), **ipykernel** (^6.30.0)
- **pytest** (^8.0.0), **black** (^24.0.0), **ruff** (^0.6.0), **mypy** (^1.13.0)

## Neo4j Access

- **Browser UI:** http://localhost:7474
- **Bolt Connection:** bolt://localhost:7687
- **Username:** neo4j
- **Password:** password123 (change in docker-compose.yml)

## Environment Setup

Copy `.env.sample` to `.env` and configure:
```bash
cp .env.sample .env
```

## Daily Workflow

```bash
# Start services
docker compose up -d

# Run tests
poetry run pytest

# Format code
poetry run black . && poetry run ruff check --fix .

# Type check
poetry run mypy src/

# Work in notebooks
poetry run jupyter lab

# Stop services
docker compose down
```
