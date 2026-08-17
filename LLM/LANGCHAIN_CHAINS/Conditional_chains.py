import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from typing import Optional,AnyStr,Dict,Annotated,Literal,List
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"))

model = ChatHuggingFace(llm=llm)
parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment :Literal['positive','neagtive']=Field(description="give the sentiment of the feedback")


parser2=PydanticOutputParser(pydantic_object=Feedback)  

prompt1 = PromptTemplate(
    template="""Classify the following feedback text into positive or negative.

Feedback:
{feedback}

{format_instruction}
""",
    input_variables=['feedback'],
    partial_variables={
        'format_instruction': parser2.get_format_instructions()
    }
)
 
classifier_chain=prompt1 |model |parser2
prompt2=PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)
prompt3=PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2 | model | parser ),
    (lambda x:x.sentiment == 'negative',prompt3 | model | parser  ),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain =classifier_chain | branch_chain

print(chain.invoke({'feedback':'this is a beautiful phone'}))
chain.get_graph().print_ascii()