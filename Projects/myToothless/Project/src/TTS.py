'''
Text To Speech
    Convert Text(String) to MP3 file
'''

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


class TTS:
    def __init__(self):
        self.speech_file_path = f"{ROOT}/audio/speech.mp3"

    def initial_tts(self):
        client = OpenAI()

        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input="Hey Shubham, what’s the vibe today?"
        )

        response.stream_to_file(self.speech_file_path)

        return 200

    def user_response(self, model_output):
        client = OpenAI()

        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=model_output
        )

        response.stream_to_file(self.speech_file_path)

        return 200