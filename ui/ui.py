import streamlit as st
import requests

st.title("RAG System")

api_url = "http://localhost:8000/api/v1/chat"

question = st.text_input("Ask a question:")
if st.button("Get Answer"):
    payload = {"messages": [{"content": question, "role": "user"}]}
    response = requests.post(api_url, json=payload)
    st.write(response.json())
