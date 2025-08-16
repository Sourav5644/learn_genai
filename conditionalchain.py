from langchain_openai import ChatOpenAi
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langcahin_core.prompts import PromptTemplate
from langchain_core.output_parsers import PromptTemplate
from langchain_core.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_Parser import PydanticOutParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv
model=ChatOpenAI()
parser=StrOutputParser()
parser2=PydanticOutParser(pydantic_object=Feedback)

class Feedback(BaseModel):
    sentiment: Literal['positive','negative']=Field(description='Give the sentiment of the feedback')

prompt1=PromptTemplate(
    template='Classify the sentiment of the following feedback text intopsitive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2}
)
classifier_chain=prompt1 | model | parser2

prompt2=PromptTemplate(
    template='write an approprpiate resons to this positive feedback \n {feedback}',
    input_variables=['feedback']

)

prompt3= PromptTemplate(
    template ='Write an appropriate response to this negative feedback \n{feedback}',
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative'. prompt3 | model | parser),
    RunnableBranch(lamda x:"could not find sentiment")
)
chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()