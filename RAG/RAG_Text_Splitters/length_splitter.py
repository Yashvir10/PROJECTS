from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader=PyPDFLoader()

docs=loader.load()

splitter = CharacterTextSplitter(
    chunk_size =100,
    chunk_overlap=0,
    seperator=''
)

result=splitter.split_documnets(docs)

print(result[0].page_content)
