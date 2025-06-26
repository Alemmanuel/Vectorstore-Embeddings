from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("mi_vectorstore", embeddings, allow_dangerous_deserialization=True)

query = "¿Qué dice el documento sobre la privacidad?"
docs = vectorstore.similarity_search(query)

for i, doc in enumerate(docs):
    print(f"\n--- Resultado {i+1} ---\n{doc.page_content}")
