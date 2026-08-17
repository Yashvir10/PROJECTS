from langchain_text_splitters import RecursiveCharacterTextSplitter,Language,CharacterTextSplitter 
from langchain_community.document_loaders import PyPDFLoader,TextLoader,AmazonTextractPDFLoader,WebBaseLoader

text="hi my name is yashvir bhardwaj . I am 21 year's old .Born in punjab on10 december 2004. currently a resident in deoli una himachal pradesh.Currently I  am working as a Remote Junior AI Enginner at Nexority Infotech,noida ,India."

#initailize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=200,
    chunk_overlap=0,
)

#perform the split
chunks=splitter.split_text(text)

print(len(chunks))
print(chunks[0])