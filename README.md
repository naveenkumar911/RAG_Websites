# Retrieval Augmented Generation (RAG) System

## Overview
This project implements a Retrieval Augmented Generation (RAG) system for answering user queries based on content scraped from specified websites. It includes features such as text scraping, embedding generation, vector database integration, and response generation with citations.

## Features
1. Index content from URLs and store embeddings in a vector database.
2. Generate answers to user questions with proper citations.
3. API-based architecture for easy integration.
4. Secure API with basic authentication.
5. Minimalistic user interface for demonstration.

---

## Requirements
- Python 3.9+
- Docker (for containerization)
- Virtual environment (recommended)

---

## Setup Instructions

### Clone the Repository
```bash
git clone <your-private-repo-url>
cd rag-system
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Usage
Run API Locally
bash
Copy code
uvicorn app.main:app --host 0.0.0.0 --port 8000
Run UI Locally
bash
Copy code
streamlit run app/ui/ui.py
Test API Endpoints
bash
Copy code
pytest tests/
API Endpoints
1. Index Endpoint
URL: /api/v1/index
Method: POST
Body:
json
Copy code
{
    "url": ["https://example.com/article"]
}
2. Chat Endpoint
URL: /api/v1/chat
Method: POST
Body:
json
Copy code
{
    "messages": [{"content": "What is late interaction?", "role": "user"}]
}
Run with Docker
Build the Docker image:

bash
Copy code
docker build -t rag-system .
Run the container:

bash
Copy code
docker run -p 8000:8000 rag-system
Deployment
You can deploy the system on platforms like AWS or Heroku using the files in deployments folder.
