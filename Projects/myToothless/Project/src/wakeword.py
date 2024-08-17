import os
import time
import pvporcupine
from pvrecorder import PvRecorder
from Project.src.TTS import TTS
from Project.src.playAudio import PlayAudio
from Project.src.record_audio import RecordAudio
from Project.src.ATS import AudioToSpeech
from Project.src.myagents import MYAGENTS
from dotenv import load_dotenv

# Load the env variable
load_dotenv()  # take environment variables from .env.

HOME = os.getcwd()
print(HOME)
ROOT = os.path.dirname(HOME)
print(ROOT)

# Initialize Audio
tts_obj = TTS()
player_obj = PlayAudio()
command_recorder_obj = RecordAudio()
ats_obj = AudioToSpeech()
agent_obj = MYAGENTS()

class WakeWord:
    def __init__(self):
        self.access_key = os.getenv('porcupine_access_key')
        self.model_path = f'{ROOT}/model/toothless_en_mac_v3_0_0/toothless_en_mac_v3_0_0.ppn'

    def wake_work(self):
        keywords = ['Toothless']


        # Initializing
        porcupine = pvporcupine.create(
                access_key=self.access_key,
                keyword_paths=[self.model_path]
        )

        devices = PvRecorder.get_available_devices()
        print(devices)
        # print(devices[-1])


        recoder = PvRecorder(device_index=0, frame_length=porcupine.frame_length)


        try:
            recoder.start()

            while True:
                keyword_index = porcupine.process(recoder.read())

                if keyword_index >= 0:
                    print("Hey, Shubham")
                    command_recorder_status_code = command_recorder_obj.record_voice_command()
                    print(command_recorder_status_code)
                    user_command = ats_obj.audio_to_string()
                    print(user_command)
                    agent_response = agent_obj.run_agent(user_command)
                    print(agent_response)
                    tts_status_code = tts_obj.user_response(agent_response)
                    print(tts_status_code)
                    audio_player_status_code = player_obj.play_audio()
                    print(audio_player_status_code)

        except KeyboardInterrupt:
            recoder.stop()
        finally:
            porcupine.delete()
            recoder.delete()

