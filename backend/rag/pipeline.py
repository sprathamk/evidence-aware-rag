from backend.ingestion.pdf_loader import extract_pages
from backend.ingestion.chunker import chunk_text
from backend.ingestion.embedder import embed_chunks
from backend.vector_db.qdrant_db import upload_chunks, fetch_chunks
from backend.generation.prompt_builder import build_prompt
from backend.generation.gemini_client import generate_response

def index_document(pdf_path):
    pages = extract_pages(pdf_path)
    chunks = chunk_text(pages)
    embeddings = embed_chunks(chunks)
    upload_chunks(chunks, embeddings)


def answer_question(query):
    chunks = fetch_chunks(query)
    prompt = build_prompt(chunks, query)

    response = generate_response(prompt)

    sources = []

    for result in chunks:
        sources.append({
            "document": result.payload["document"],
            "page": result.payload["page"],
            "chunk": result.payload["chunk_index"],
            "score": result.score,
            "text": result.payload["text"]
        })

    return {
        "answer": response,
        "sources": sources
    }