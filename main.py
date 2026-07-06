from backend.ingestion.pdf_loader import extract_text
from backend.ingestion.chunker import chunk_text
from backend.ingestion.embedder import embed_chunks

text = extract_text("data/sample.pdf")
chunks = chunk_text(text)
embeddings = embed_chunks(chunks)

print(f"Length of chunks{len(chunks)}")
print("No of embeddings", len(embeddings[0]))