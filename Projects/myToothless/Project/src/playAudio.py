import os
import subprocess

HOME = os.getcwd()
ROOT = os.path.dirname(HOME)

class PlayAudio:
    def __init__(self):
        self.audio_file = f'{ROOT}/audio/speech.mp3'

    def play_audio(self):
        return_code = subprocess.call(["afplay", self.audio_file])
        return 200