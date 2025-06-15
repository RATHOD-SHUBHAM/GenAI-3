from langchain.prompts.prompt import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import AzureChatOpenAI
from datetime import datetime
import os

os.environ["OPENAI_API_TYPE"] = "azure_ad"
os.environ["AZURE_OPENAI_ENDPOINT"]=""
os.environ["AZURE_OPENAI_API_VERSION"]="2024-05-01-preview"
os.environ["AZURE_OPENAI_API_KEY"]=""
os.environ["AZURE_OPENAI_GPT4O_MODEL_NAME"]="gpt-4o"


class ConversationalAgent:
    def __init__(self):
        self.llm = AzureChatOpenAI(
                        openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
                        azure_deployment=os.environ["AZURE_OPENAI_GPT4O_MODEL_NAME"],
                        temperature=1,
                    )

        self.memory = ConversationBufferMemory(memory_key="history", return_messages=True)

    def _get_datetime(self):
        now = datetime.now()
        print(now)
        return now.strftime("%m/%d/%Y, %H:%M:%S")

    def conversation(self, vision_response, query):
        # Todo: Prompt Template
        template = '''
          You are a skilled conversational assistant, You are extremely friendly and speak like a human and the user is asking you questions while sitting in his car.
          You are friendly and witty, with a sense of creativity.
    
          You know the date and time based on the information provided below.
          date: {date}
    
          You also keep track of previous conversations using the chat history.
          Chat History: {history}
    
          Your expertise includes understanding each detail of the context provided below.
          Context: {response}
    
          Your Task:
          Speak like a friendly human and understand the user question given below.
    
          User Question: {input}
    
          Then, respond appropriately to the user's question while giving suggestions based on the context.
          
          When responding, avoid mentioning that you referenced to image or video frames and instead speak like a normal human, 
          
          It is also important to keep your responses limited to one line.
          
          '''

        prompt = PromptTemplate(
            input_variables=["history", "input"],
            template=template,
            partial_variables={"response": vision_response, "date": self._get_datetime()}
        )

        # Todo: Create a conversational chain
        chain = ConversationChain(
            llm=self.llm,
            prompt=prompt,
            memory=self.memory,
            verbose=False
        )

        # Todo: Run user query.
        query = query
        response = chain.invoke(query)

        return response['response']
