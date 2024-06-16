'''
Google Docs:
    https://ai.google.dev/gemini-api/docs?_gl=1*83sq00*_ga*Mjc0MzgwOTkyLjE3MTU4MjA4MTI.*_ga_P1DBVKWT6V*MTcxODQ2MzUwNC4xNC4xLjE3MTg0NjM1MzAuMzQuMC4xNjkxOTQxODUy

'''

import os
import google.generativeai as genai
from dotenv import load_dotenv
from langchain.prompts import load_prompt

# Todo: Load env
load_dotenv()  # Load all the evironment variables
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Todo: Config Path
HOME = os.getcwd()  # Current working dir
ROOT = os.path.dirname(HOME)  # Parent dir

# Todo: Load the prompt
prompt_file = f'{HOME}/prompts/summarize_prompt.json'
# print(prompt_file)
prompt = load_prompt(prompt_file)
# print(prompt.template)


# Todo: Generate Content
def generate_notes(transcript):
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(prompt.template + transcript)

    return response.text