from API import * 
# Imports {
    # sys 
    # textToSpeech {speech_recognition as sr}
    # BOOT {os, pandas as pd, PasswordGenerator}
    # BootMails {SendMails}
    # OpenFile
# }

# Boot()


def Start():
    print("Go ahead! I'm listening ...")
    engine.say("Go ahead! I'm listening ...")
    engine.runAndWait()
    text = speak()
    # text = "scan"
    print(text)
    Command(text)
    
if __name__ == '__main__':
    Boot()
    while True:
        c = input("Enter space to start or any other character to exit: ")
        if c == " ":
            Start()
        else:
            exit()
