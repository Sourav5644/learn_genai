from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchian.schema import RunnableSequence, RunnableParallel,RunnablePassthrough
load_dotenv()

prompt1=PromptTemplate(
    template='Write a joke about{topic}',
    input_variables=['topic']
)
model=ChatOpenAI()
parser=StrOutputParser()

prompt2=PromptTemplate(
    template='exaplin the following joke -{text}',
    input_variables=['text']
)

joke_gen_chian=RunnableSequence(prompt1 | model | parser)

parallel_chain=RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination':(prompt2 | model | parser)
})

final_chain=RunnableSequence(joke_gen_chian | parallel_chain)

print(final_chain.invoke({'topic':'cricket'}))
