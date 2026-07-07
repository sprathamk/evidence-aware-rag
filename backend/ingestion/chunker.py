from typing import List


def chunk_text(pages, chunk_size=500, overlap=100,):

    chunks = []

    chunk_index = 0

    for page in pages:

        text = page["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunks.append(
                {
                    "text": text[start:end],
                    "page": page["page"],
                    "document": page["document"],
                    "chunk_index": chunk_index,
                }
            )

            chunk_index += 1

            start += chunk_size - overlap

    return chunks