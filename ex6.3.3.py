import pyttsx3

engine = pyttsx3.init()

sentence = "first time i'm using a package in next.py course"

engine.say(sentence)
engine.runAndWait()
