# Todo: Import Libraries
import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts.prompt import PromptTemplate
# from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain

HOME = os.getcwd()

# Todo: Memory
memory = ConversationBufferMemory(memory_key="chat_history", input_key='question', output_key='answer', return_messages=True)

# Todo: Embedd
embeddings = OllamaEmbeddings(model='znbang/bge:large-en-v1.5-q4_k_m')

# Todo: load from disk
persist_directory = f'{HOME}/chroma_db'
index = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

# Todo: Retriever
retriever = index.as_retriever(search_type="mmr")

# Todo: Prompt
custom_template = """
    You are an Expert AI assistant designed to answer user questions based on the content of a provided document. 
    Please ensure that all answers are strictly derived from the information within the document. 
    Do not include any external knowledge or assumptions in your responses
    
    Provide the answer directly without prefacing it with phrases like "According to the provided context" or "Based on the provided context" or similar.
        
    Chat History:
    {chat_history}
    
    question: {question}
    
    answer: 
    
    Example Usage:
    question: What does mobility solutions enable?
    answer: The connected mobility solutions enable the mobility ecosystem players to provide a personalized experience , monetize the data and enable new business models.


"""

# Todo: Generate Response
llm = ChatOllama(model="llama3.1:latest", temperatur=0)

# question = 'Can you describe Hydrogen Passport ?'

while True:
    question = input("Ask: ")

    if question == 'q':
        break

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        verbose=True,
        memory=memory,
        return_generated_question=True,
        retriever=retriever,
        condense_question_prompt=PromptTemplate.from_template(custom_template)
    )

    result = qa_chain.invoke(question)
    print(result)
    # print(result['chat_history'][1])
    # print(type(result['chat_history'][1]))
    print(result['chat_history'][1].content)