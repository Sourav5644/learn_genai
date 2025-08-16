from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompt import PrompTemplate
from langcahin_core.output_parsers import StrOutputParser

load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task='text-generation'
)
model=ChatHuggingFace(llm=llm)

template1=PrompTemplate(
    template='Write a detailed report on {topic}',
    input_variable=[text]

)
template2=PrompTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser= StrOutputParser()

chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({'topic':'black hole'})
print(result)