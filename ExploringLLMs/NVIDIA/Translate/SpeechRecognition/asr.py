# on MacOS using Homebrew (https://brew.sh/)
# brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
# choco install ffmpeg
import whisper

model = whisper.load_model("turbo")
result = model.transcribe("/Users/shubhamrathod/PycharmProjects/NVIDIA/Translate/SpeechRecognition/microphone-results.wav")
print(result["text"])