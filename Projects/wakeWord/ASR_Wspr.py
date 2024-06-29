import whisper

model = whisper.load_model("small.en")
result = model.transcribe("audio/my_recording.wav")
print(result["text"])