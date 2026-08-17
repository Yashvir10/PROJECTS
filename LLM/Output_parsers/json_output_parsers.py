# the biggest flow of jason is the that it does not enforse a Schema 
import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import JsonOutputParser



load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"))

model = ChatHuggingFace(llm=llm)

parser=JsonOutputParser

template = PromptTemplate(
    template='give me the name , age , city of a frictional character \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instruction()}
)

# prompt =template.format()
# result=model.invoke(prompt)
# final_result =parser.parse(result.content)
# print(final_parser)


""""by using chains in the code"""
chain=template | model | parser
result=chain.invoke({})
print(result)

