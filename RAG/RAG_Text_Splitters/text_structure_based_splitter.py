from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

text="hi my name is yashvir bhardwaj . I am 21 year's old .Born in punjab on10 december 2004. currently a resident in deoli una himachal pradesh.Currently I  am working as a Remote Junior AI Enginner at Nexority Infotech,noida ,India."

#Initailaizing the Splitter 
splitter=RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0,
)

#perform the split 
chunks=splitter.split_text(text)

print(len(chunks))
print(chunks)
