import os
os.environ['OPEN_API_KEY']='sk-proj-ORV1HwUGs8R8vWlaRYLdAzJfhxLH9NYWyb5GDGGm9Il4JLsPWQX5L1I8A9hR_Cbs1a0JWaPCtUdqvv5LRedP2mIWl8A'

#install libraries in env are:
# -q youtube -transcript-api langchain-community langchain-openai \ 
#  faiss-cpu tiktoken python-dotenv

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

## Step 1-Indexing(Document Ingestion)

video_id='Gfr889779hjg' # only the videoid not the full url plz
try:
    # if you don't care which language, this returns the 'best' one
    transcript_list=YouTubeTranscriptApi.get_transcript(video_id, language=['en'])
    # Flatten it to plain text
    transcript=" ".join(chunk['text'] for chunk in transcript_list)
    print(transcript)
except TranscriptsDisabled:
    print('No captons available for this video.')  


#Step 1b-Indexing(Text Splitting)
splitter=RecursiveCharacterTextSplitter(chun_size=1000, chunk_overlap=200)
chunks=splitter.create_documents([transcript])
print(len(chunks))

# Step 2- Indexing(Embedding Generation and storing in Vector Store)
embeddings=OpenAIEmbeddings(model='text-embedding-3-small')
view=vector_store.index_to_docstore_id
print(view)

## Step-3 Retrieval

retriever= vector_store.as_retriever(search_type='similarity',search_kwargs={'k':4})
print(retriever)

retriever.invoke('what is deepmind')

#step-3 Augmentation

llm=ChatOpenAI(model='gpt-4o-mini',temperature=0.2)

prompt=PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables=['context','question']

)

question="is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
retrieved_docs =retriever.invoke(question)

context_text="\n\n".join(doc.page_content for doc in retrieved_docs)
context_text

final_prompt=prompt.invoke({'context': context_text, 'question':question})

# Step 4-Generation
answer= llm.invoke(final_prompt)
print(answer.content)

from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parser import StrOutputParser

def format_docs(retrieved_docs):
    content_text= "\n\n".join(doc.page_conent for doc in retrieved_docs)
    return content_text


parallel_chain=RunnableParallel({
    'context':retriever | RunnableLambda(format_docs),
    'question':RunnablePassthrough()
})

parallel_chain.invoke('who is Demis')
parser=StrOutputParser()
main_chain=parallel_chain | prompt | llm | parser
main_chain.invoke('Can you summarize the video')



