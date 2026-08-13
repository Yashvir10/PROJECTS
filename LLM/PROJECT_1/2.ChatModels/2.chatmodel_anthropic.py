from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
model = ChatAnthropic(model='claude-v1', temperature=0.5, max_completion_tokens=100)
result = model.invoke("What is the capital of France?")
print(result.content)