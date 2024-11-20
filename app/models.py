from transformers import pipeline

qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(question, snippets):
    context = " ".join([s["content"] for s in snippets])
    result = qa_pipeline(f"Question: {question} Context: {context}")
    answer = result[0]["generated_text"]
    citations = [s["url"] for s in snippets]
    return answer, citations
