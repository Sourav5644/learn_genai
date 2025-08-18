from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.documents import Document

# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embedding_model=OpenAIEmbeddings()
vectorstore=Chroma.form_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name='my_collection'
)

retriever=vectorstore.as_reteriver(search_kwargs=["k":2])

query="what is chroma used for ?"
result=retriever.invoke(query)for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)