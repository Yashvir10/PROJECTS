from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='//load your csv here //')

docs=loader.load()

print(len(docs))
print(docs[1])

print(docs[0].page_content)
