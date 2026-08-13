from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from torch import embedding

load_dotenv()  # Load environment variables from .env file

embeddings = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents=[
    "delhi is the capital of india",
    "kolkata is the capital of west bengal",
    "paris is the capital of france",
]
result=embeddings.embed_documents(documents)

print(str(result))