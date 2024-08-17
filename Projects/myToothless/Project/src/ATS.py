import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the env variable
load_dotenv()  # take environment variables from .env.

HOME = os.getcwd()
# print(HOME)
ROOT = os.path.dirname(HOME)
# print(ROOT)
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

class AudioToSpeech:
  def __init__(self):
    self.file_path = f'{ROOT}/audio/command.wav'

  def audio_to_string(self):

    client = OpenAI()

    audio_file= open(self.file_path, "rb")

    transcription = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file
    )

    user_input = transcription.text
    print(user_input)

    return user_input