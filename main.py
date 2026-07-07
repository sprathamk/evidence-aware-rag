from backend.rag.pipeline import answer_question, index_document

index_document("data/sample.pdf")

query = "what is encoder"

answer = answer_question(query)

print(answer)
