# main.py
from src.test2 import get_rag_chain

retrieval_chain = get_rag_chain()

question = "How do I create a scene with a circle that turns into a square?"
response = retrieval_chain.invoke({"input": question})

print("\n--- Generated Code ---\n")
print(response["answer"])
