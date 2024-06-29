import os

# LLM
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

access_key = os.getenv('access_key')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')