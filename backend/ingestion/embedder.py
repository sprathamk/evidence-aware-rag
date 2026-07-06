from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")


def embed_chunks(chunks):
  
    embeddings = model.encode(chunks)

    return embeddings