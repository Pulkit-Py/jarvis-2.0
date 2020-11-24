import speech_recognition as sr
def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Lisiting...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognition.....")
        cmd = r.recognize_google(audio)
    except Exception as e:
        print("please say that again")
        return "None"
    print("user: "+ cmd)    
    return cmd