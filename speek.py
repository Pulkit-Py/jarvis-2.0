import pyttsx3
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
def sp(audio):
    engine.say(audio)
    engine.runAndWait()

