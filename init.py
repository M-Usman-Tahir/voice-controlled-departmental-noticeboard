from functions import * 
# Imports {
    # sys 
    # textToSpeech {speech_recognition as sr}
    # BOOT {os, pandas as pd, PasswordGenerator}
    # BootMails {SendMails}
    # OpenFile
# }

# LogIN("2019-CE-34")

# Boot()
# print("Opening the public Notifications...")
# OPEN(os.path.join("Notis", "Noti.jpeg"))

import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def Start():
    engine.say("Waiting for you command!")
    engine.runAndWait()
    # text = speak(engine)
    text = "scan"
    print(text)
    Command(engine, text)
    
if __name__ == '__main__':
    while True:
        c = input("Enter space to start or any other character to exit: ")
        if c == " ":
            Start()
        else:
            exit()
