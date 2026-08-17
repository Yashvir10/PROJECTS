# this fils is made to show the Dynamic Messages used in a list of messages 
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

chat_template=ChatMessagePromptTemplate=(
    ('system','you are a helpful {domain} expert'),
    ('human','explain in simple terms , what is {topic}')
)

result=chat_template.invoke({'domain':'criket','topic':'dusra'})
print(result)