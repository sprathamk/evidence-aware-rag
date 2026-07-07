from backend.ingestion.pdf_loader import extract_text
from backend.ingestion.chunker import chunk_text
from backend.ingestion.embedder import embed_chunks
from backend.retrieval.search import retrieve
from backend.vector_db.qdrant_db import upload_chunks, fetch_chunks

text = extract_text("data/sample.pdf")
chunks = chunk_text(text)
embeddings = embed_chunks(chunks)

upload_chunks(chunks, embeddings)

results = fetch_chunks("what is encoder")

for result in results:
    print("Score:",result.score)
    print("Chunk id:", result.payload["chunk_index"])
    print(result.payload["chunk"])
    print("=" * 50)