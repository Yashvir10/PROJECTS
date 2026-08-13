from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv  

load_dotenv()  # Load environment variables from .env file

model = ChatGoogleGenAI(model='chat-bison-001', temperature=0.5, max_completion_tokens=100)

result = model.invoke("What is the capital of France?")

print(result.content)