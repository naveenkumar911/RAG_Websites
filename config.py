import os
from dotenv import load_dotenv

load_dotenv()

# API Authentication Key
API_KEY = os.getenv("API_KEY", "default_key")

# Embedding Model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Vector Database
VECTOR_DB_DIMENSION = 384
