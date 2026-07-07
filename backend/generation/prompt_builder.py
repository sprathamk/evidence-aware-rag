def build_prompt(chunks, query):

    context = ""

    for chunk in chunks:
        context += f"=== Retrieved Chunk {chunk.payload["chunk_index"]} === \n"
        context += chunk.payload["chunk"]
        context += "\n"
    
    prompt = f"""You are a research assistant.
    Use ONLY the retrieved context below.
    If the answer is not contained in the context,
    reply: "I couldn't find enough evidence in the retrieved documents."
    Do not make assumptions.
    Do not use outside knowledge.Retrieved Context:
    {context} 
    Question:{query}
    Answer:"""

    # print(prompt)

    # print("*" * 50)

    return prompt
