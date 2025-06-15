import os

from google import genai
from dotenv import load_dotenv

load_dotenv()  # take environment variables

google_api_key = os.getenv('google_api_key')

client = genai.Client(api_key=google_api_key)

myfile = client.files.upload(file='microphone-results.wav')

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents=['Transcribe this audio clip', myfile]
)

print(response.text)