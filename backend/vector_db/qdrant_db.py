from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from backend.ingestion.embedder import model

COLLECTION_NAME = "research_papers"

client = QdrantClient("localhost", port=6333)

def upload_chunks(chunks, embeddings):

    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=len(embeddings[0]), distance=Distance.COSINE),
        )

    data_points = []

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        data_points.append(
            PointStruct(
                id=i,
                vector=embedding.tolist(),
                payload={
                    "text": chunk["text"],
                    "page": chunk["page"],
                    "document": chunk["document"],
                    "chunk_index": chunk["chunk_index"],
                }
            )
        )
    
    operation_info = client.upsert(
      collection_name=COLLECTION_NAME,
      wait=True,
      points=data_points,
    )

    return operation_info


def fetch_chunks(query):
    query_embedding = model.encode(query)

    search_result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        with_payload=True,
        limit=3
    ).points

    return search_result

