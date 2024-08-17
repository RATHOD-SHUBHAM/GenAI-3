from Project.src.TTS import TTS
from Project.src.playAudio import PlayAudio


# Initialize Audio
tts_obj = TTS()
player_obj = PlayAudio()

class Greeting:
    def greet(self):
        tts_status_code = tts_obj.initial_tts()
        print(tts_status_code)
        audio_player_status_code = player_obj.play_audio()
        print(audio_player_status_code)