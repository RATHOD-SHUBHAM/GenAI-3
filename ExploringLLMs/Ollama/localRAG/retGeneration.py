# Todo: Import Libraries
import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain

HOME = os.getcwd()

# Todo: Embedd
embeddings = OllamaEmbeddings(model='znbang/bge:large-en-v1.5-q4_k_m')

# Todo: load from disk
persist_directory = f'{HOME}/chroma_db'
index = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

# Todo: Retriever
retriever = index.as_retriever(search_type="mmr")

# Todo: Generate Response
llm = ChatOllama(model="llama3.1:latest", temperatur=0)

query = 'Can you describe Hydrogen Passport ?'

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

result = qa_chain.invoke({'query': query})
# print(result)
print(result['result'])
print("/n/n")
print(result['source_documents'])