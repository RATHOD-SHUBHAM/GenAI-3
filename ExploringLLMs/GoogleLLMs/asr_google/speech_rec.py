import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please say something...")
    audio = r.listen(source)

# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

