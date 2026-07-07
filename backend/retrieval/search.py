from backend.ingestion.embedder import model
import numpy as np


def cosine_similarity(vec1, vec2):

    dot_product = np.dot(vec1, vec2)

    norm_vec1 = np.linalg.norm(vec1)

    norm_vec2 = np.linalg.norm(vec2)

    similarity = dot_product / (norm_vec1 * norm_vec2)

    return similarity


def retrieve(query, chunks, embeddings, top_k=3):

    query_embedding = model.encode(query)

    scores = []

    for i, embedding in enumerate(embeddings):

        score = cosine_similarity(query_embedding, embedding)

        scores.append((score, chunks[i], i))

    scores.sort(reverse=True)

    return scores[:top_k]