from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

#1 prompt
template1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)
#2 prompt
template2=PromptTemplate(
    template='write a 5 line summary on the following text. /n {text}',
    input_variable=['text']
)
prompt1=template1.invoke({'topic':'black hole'})
result=model.invoke(prompt1)

prompt2=template2.invoke({'text':result.content})
result=model.invoke(prompt2)
print(result.content)


