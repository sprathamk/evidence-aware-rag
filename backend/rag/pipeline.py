from backend.ingestion.pdf_loader import extract_text
from backend.ingestion.chunker import chunk_text
from backend.ingestion.embedder import embed_chunks
from backend.vector_db.qdrant_db import upload_chunks, fetch_chunks
from backend.generation.prompt_builder import build_prompt
from backend.generation.gemini_client import generate_response

def index_document(pdf_path):
    text = extract_text(pdf_path)
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)
    upload_chunks(chunks, embeddings)


def answer_question(query):
    chunks = fetch_chunks(query)
    prompt = build_prompt(chunks, query)

    response = generate_response(prompt)

    return response