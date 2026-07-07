from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

def embed_chunks(chunks):

    texts = []

    for chunk in chunks:
        texts.append(chunk["text"])

    embeddings = model.encode(texts)

    return embeddings