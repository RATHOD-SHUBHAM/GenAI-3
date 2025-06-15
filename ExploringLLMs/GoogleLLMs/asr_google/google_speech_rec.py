import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please say something...")
    audio = r.listen(source)

# Use Google's speech recognition service to convert audio to text
try:
    text = r.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from the speech recognition service; {e}")
