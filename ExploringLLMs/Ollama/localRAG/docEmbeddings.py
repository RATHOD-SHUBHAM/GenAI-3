# Todo: Import Libraries
import os
# from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# Get file Path
HOME = os.getcwd()
file_path = f'{HOME}/faq.pdf'

# Todo: Load document
# loader = TextLoader(file_path)
loader = PyPDFLoader(file_path)
pages = loader.load()

# Todo: Chunk the Document
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=10000,
    chunk_overlap=3000,
    length_function=len,
    is_separator_regex=False,
)

docs = text_splitter.split_documents(pages)
# print(docs)

# Todo: Embedd the document
embeddings = OllamaEmbeddings(model = 'znbang/bge:large-en-v1.5-q4_k_m')
# embeddings = OllamaEmbeddings(model = 'mxbai-embed-large:latest')


# Todo: save to disk
persist_directory="chroma_db"
index = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)

# Todo: Check for the index
docs = index.similarity_search('Describe Autonomous vehicle solutions in Brief ?')
print(docs)