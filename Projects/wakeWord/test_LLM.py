# Todo: Load libraries
import os
from dotenv import load_dotenv

# Todo: Getting the access key
load_dotenv()  # take environment variables from .env.
access_key = os.getenv('access_key')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

template = """Question: {question}

Answer: """

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI(model_name="gpt-3.5-turbo-instruct", openai_api_key = OPENAI_API_KEY)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "Take me to office"

print(llm_chain.run(question))

