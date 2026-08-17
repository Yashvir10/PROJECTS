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

prompt1=PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='Generate a 5 pointer summary on the following text\n {text}',
    input_variables=['text']
)
model = ChatHuggingFace(llm=llm)
parser=StrOutputParser()
chain=prompt1 | model | parser | prompt2 |model | parser

result =chain.invoke({'topic':'unemployment in India'})

print(result)

chain.get_graph().print_ascii()