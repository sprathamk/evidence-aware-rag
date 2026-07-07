from backend.rag.pipeline import answer_question, index_document

index_document("data/sample.pdf")

query = "what is encoder"

answer = answer_question(query)

print(answer["answer"])
print("\nSources")

sources = answer["sources"]

for source in sources:
    print(f"Document : {source['document']}")
    print(f"Page     : {source['page']}")
    print(f"Chunk ID : {source['chunk']}")
    print(f"Score    : {source['score']}")
    print(f"Text     : {source['text'][:97]}...")
    print("-" * 40)


