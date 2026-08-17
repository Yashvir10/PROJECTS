import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"))

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str=Field(description='name of the person')
    age :int=Field(gt=18,lt=100,description="age of the person ")
    city:str=Field(description="the city in which the person lives")

parser=PydanticOutputParser(pydantic_object=Person)
template =PromptTemplate(
    template='Generate the name , age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()} 
)
# prompt =template.invoke({'place':'India'})

# result=model.invoke(prompt)

# final_result=parser.parse(result.content)

# print(final_result)

chain=template|model|parser
result=chain.invoke({'place':"indian"})
print(result)