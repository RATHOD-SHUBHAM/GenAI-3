# on MacOS using Homebrew (https://brew.sh/)
# brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
# choco install ffmpeg

# import whisper
import os
from openai import OpenAI

# Load the environments
HOME = os.getcwd()
ROOT = os.path.dirname(HOME)
BASE_DIR = os.path.dirname(HOME)
# Todo: My openai key
os.environ[
    'OPENAI_API_KEY'] = ''


# Todo: Local Model
# def run_asr():
#     model = whisper.load_model("turbo")
#     file_path = f'{HOME}/src/utils/microphone-results.wav'
#     result = model.transcribe(file_path)
#     # print(result["text"])
#     return result["text"]

# Todo: API call
def run_asr():
    client = OpenAI()
    audio_file_path = f'{HOME}/src/utils/microphone-results.wav'
    audio_file = open(audio_file_path, "rb")

    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    # print(transcription)

    return transcription
