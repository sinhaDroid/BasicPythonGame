import speech_recognition as sr

# Use audio file as source
AUDIO_FILE = ("harvard.wav")

# Initialise the recogniser
r = sr.Recognizer() 

# Reads the audio file
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try :
    print("audio file contains " + r.recognize_google(audio))
except sr.UnknownValueError :
    print("Google Speech Recognition could not understand audio")
except sr.RequestError :
    print("Couldn't get the results from Google Speech Recognition")