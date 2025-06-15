import speech_recognition as sr
import os
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = ''

HOME = os.getcwd()
# print(HOME)
ROOT = os.path.dirname(HOME)
# print(ROOT)
BASE_DIR = os.path.dirname(HOME)
# print(BASE_DIR)

def record_audio():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=5)

    # write audio to a WAV file
    file_path = f'{HOME}/audio/microphone-results.wav'
    with open(file_path, "wb") as f:
        f.write(audio.get_wav_data())


record_audio()

def run_asr():
    client = OpenAI()
    audio_file_path = f'{HOME}/audio/microphone-results.wav'
    audio_file = open(audio_file_path, "rb")

    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    print(transcription)

    return transcription

# run_asr()