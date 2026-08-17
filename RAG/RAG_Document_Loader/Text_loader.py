import os
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"))

model = ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt=PromptTemplate(
    template='wriyte the summary for thr following poem - \n {poem}',
    input_variables=['poem']
)

loader = TextLoader('cricket.txt',encoding='utf-8')

docs=loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain=prompt | model |parser
result=(chain.invoke({'poem':'docs[0].page_content'}))
print(result)