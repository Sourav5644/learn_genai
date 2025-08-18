import os
os.environ["OPEN_API_KEY"]="sk-proj-a0huhdiobidhjdjij"
# pip install langchain chromadb faiss-cpu openai tiktoken langchain_openai langchain
#Wikipedia Retriever

from langchain_community.retrievers import WikipediaRetriever
retreiver=WikipediaRetriever(top_k_results=2,len='eng')
query="the geopolitical history of india and pakistan from the perspective of kashmir"
docs=retreiver.invoke(query)
print(docs)

#print retrieved content

for i, doc in enumerate(docs):
    print(f'\n--Result{i+1}--')
    print(f'content:\n{doc.page_content}...')

