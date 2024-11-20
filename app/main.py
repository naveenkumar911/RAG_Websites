from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from app.utils import scrape_website, process_text
from app.db import store_embeddings, query_embeddings
from app.models import generate_answer
from app.auth import authenticate

app = FastAPI()

class IndexRequest(BaseModel):
    url: list[str]

class ChatRequest(BaseModel):
    messages: list[dict]

@app.post("/api/v1/index")
async def index(request: IndexRequest, user=Depends(authenticate)):
    indexed_urls = []
    failed_urls = []
    for url in request.url:
        try:
            text = scrape_website(url)
            processed_text = process_text(text)
            store_embeddings(processed_text, url)
            indexed_urls.append(url)
        except Exception as e:
            failed_urls.append(url)
    return {"status": "success", "indexed_url": indexed_urls, "failed_url": failed_urls}

@app.post("/api/v1/chat")
async def chat(request: ChatRequest, user=Depends(authenticate)):
    try:
        query = request.messages[-1]["content"]
        retrieved_snippets = query_embeddings(query)
        response, citations = generate_answer(query, retrieved_snippets)
        return {"response": {"content": response, "role": "assistant"}, "citation": citations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
