import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said


speak("hello and welcome, how can I help you")

text = get_audio()

if "what is your name" in text:
    speak("My name is Robot")

if "how are you" in text:
    speak("I am fine thank you, and what about you?")


if "how old are you" in text:
    speak("sorry it is not your business")


if "are you stupid" in text:
    speak("no, I am smart")

if "are you donkey" in text:
    speak("no I am robot")

if "camera" in text:
    speak("ok sir")
    os.system('/usr/bin/cheese')

if "music" in text:
    speak("ok sir")
    os.system('/usr/bin/drumstick-vpiano')
