import speech_recognition as sr
import os

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
    file_path = f'{HOME}/src/utils/microphone-results.wav'
    with open(file_path, "wb") as f:
        f.write(audio.get_wav_data())