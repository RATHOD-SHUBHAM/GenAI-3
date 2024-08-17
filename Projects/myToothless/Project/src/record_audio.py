import os
import time
from pvrecorder import PvRecorder
import wave, struct

HOME = os.getcwd()
ROOT = os.path.dirname(HOME)
# print(ROOT)

class RecordAudio:
    def __init__(self):
        self.path = f'{ROOT}/audio/command.wav'

    def list_devices(self):
        for index, device in enumerate(PvRecorder.get_available_devices()):
            print(f"[{index}] {device}")

    def record_voice_command(self):

        # (32 milliseconds of 16 kHz audio)
        recorder = PvRecorder(device_index=0, frame_length=512)
        audio = []

        try:
            recorder.start()
            print("Here")
            while True:
                frame = recorder.read()
                audio.extend(frame)
        except KeyboardInterrupt:
            recorder.stop()
            with wave.open(self.path, 'w') as f:
                f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
                f.writeframes(struct.pack("h" * len(audio), *audio))
        finally:
            recorder.delete()


        return 200