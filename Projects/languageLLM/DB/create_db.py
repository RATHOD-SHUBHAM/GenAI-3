import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings
from langchain_openai import AzureChatOpenAI
from langchain_chroma import Chroma

# Todo: Load Environments
HOME = os.getcwd()
# print(HOME)
ROOT = os.path.dirname(HOME)
# print(ROOT)
BASE_DIR = os.path.dirname(HOME)
# print(BASE_DIR)

os.environ["OPENAI_API_TYPE"] = "azure_ad"
os.environ["AZURE_OPENAI_ENDPOINT"] = ""
os.environ["AZURE_OPENAI_API_VERSION"] = "2024-05-01-preview"
os.environ["AZURE_OPENAI_API_KEY"] = ""
os.environ["AZURE_OPENAI_GPT4O_MODEL_NAME"] = "gpt-4o"


class Create_DB:

    def __init__(self):
        self.embeddings = AzureOpenAIEmbeddings(
            model="text-embedding-3-large",
        )

        self.llm = AzureChatOpenAI(
                    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
                    azure_deployment=os.environ["AZURE_OPENAI_GPT4O_MODEL_NAME"],
                    temperature=1,
                )

        # Todo: Load Document
        self.file_path = f'{HOME}/data_file/my_docs'
        # print(file_path)

        self.persist_directory = f'{HOME}/DB/my_db'

    def create_embeddings(self, chunk_size, chunk_overlap):

        loader = PyPDFLoader(
            file_path=self.file_path
        )

        docs = loader.load()

        # Todo: Chunk Document
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap,
            length_function = len,
            is_separator_regex=False

        )

        texts = text_splitter.split_documents(docs)

        # Todo: Embedding Model
        embeddings = self.embeddings

        # Vector Store
        persist_directory=self.persist_directory

        db = Chroma.from_documents(
          documents=texts,
          embedding=embeddings,
          persist_directory=persist_directory
        )

        return True

