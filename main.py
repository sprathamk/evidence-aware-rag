from backend.ingestion.pdf_loader import extract_text
from backend.ingestion.chunker import chunk_text

text = extract_text("data/sample.pdf")
chunks = chunk_text(text)

print(f"Length of chunks{len(chunks)}")
print(chunks[0],"\n\n\n\n", chunks[1])