# a directory is used to work on a folder consisting of many pdf 
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
loader= DirectoryLoader(
    path="""load your folder here""",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.lazy_load()

print(docs[325].page_content)