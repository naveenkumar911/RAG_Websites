from fastapi import HTTPException, Header

API_KEYS = {"secret_key_123": "user"}

def authenticate(api_key: str = Header(...)):
    if api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return API_KEYS[api_key]
