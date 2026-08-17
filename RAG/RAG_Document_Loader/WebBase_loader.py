from langchain_community.document_loaders import WebBaseLoader
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

prompt=PromptTemplate(
    template='Answer the following question \n {question} - \n {text}',
    input_variables=['question','text']
)

parser=StrOutputParser()

url="https://www.amazon.in/Apple-2026-MacBook-Laptop-chip/dp/B0GR64G4H6/ref=sr_1_2_sspa?crid=PYJZHXJ8O2DY&dib=eyJ2IjoiMSJ9.NYW2JjuShp6rJOMX8U9UbRdZxKylboXj_t0D3mJcGOSSwfe5307oKXQU7heiV6fqrI0ptNWYp4S-NQm9PDo7WnfyMRCLJKzlR-JWCIdpajemCeVUKg8vYasx1juZjsEd4cvj5Gsey-oQivbBbiOyhZEZqKA6MfDVtWz-UKn8zNGxFU78ooiOk28V0A8-QWQ2KlQIZyogusQiZ5d-U-qvLUq78hGVD-DVfTHpOnxF1zI.marvjzg-279_KFw87v_vZk7xretephvySKkjZzEfF2A&dib_tag=se&keywords=macbook%2Bair%2Bm4&qid=1786867232&sprefix=macbook%2Caps%2C310&sr=8-2-spons&aref=ROc9vzcamf&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
loader=WebBaseLoader(url)

docs=loader.load()

chain =prompt | model | parser
print(chain.invoke({'question':'What is the product we are talking about ?','text':docs[0].page_content}))