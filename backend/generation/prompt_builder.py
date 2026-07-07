def build_prompt(chunks, query):

    context = ""

    for chunk in chunks:

        context += (
            f"\n=== Retrieved Chunk {chunk.payload['chunk_index']} ===\n"
            f"Document : {chunk.payload['document']}\n"
            f"Page     : {chunk.payload['page']}\n\n"
            f"{chunk.payload['text']}\n\n"
        )

    prompt = f"""
You are a research assistant.

Instructions:
- Answer ONLY using the retrieved context.
- If the answer is not present, say:
"I couldn't find enough evidence in the retrieved documents."
- Do not use outside knowledge.

Retrieved Context
=================

{context}

Question
========

{query}

Answer
======
"""

    # print(prompt)

    # print("*" * 50)

    return prompt
