from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
dimension = 384
index = faiss.IndexFlatL2(dimension)
metadata = []

def store_embeddings(text, url):
    embeddings = model.encode([text])
    index.add(np.array(embeddings))
    metadata.append({"url": url, "content": text})

def query_embeddings(query, top_k=5):
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), top_k)
    results = [{"content": metadata[i]["content"], "url": metadata[i]["url"]} for i in indices[0]]
    return results
