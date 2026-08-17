import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"))

model = ChatHuggingFace(llm=llm)



# 1st prompt
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variable=['topic']
)

#2st prompt
template2 = PromptTemplate(
    template='write a five line summary on the following text./n {text}',
    input_variable=['topic']
)

parser = StrOutputParser()

chain=template1 | model | parser | template2 | model

result=chain.invoke({'topic':'black hole'})

print(result)