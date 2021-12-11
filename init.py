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
    engine.say("Waiting for you command!")
    engine.runAndWait()
    text = speak()
    # text = "scan"
    print(text)
    Command(text)
    
if __name__ == '__main__':
    Boot()
    # if not os.path.exists(os.path.join(os.getcwd(), "LOCAL")):
    #     Boot()
    # else:
    #     Bool = input("Do you want to reboot the system (Y/N): ").lower()
    #     if Bool == "y":
    #         Boot()
    while True:
        c = input("Enter space to start or any other character to exit: ")
        if c == " ":
            Start()
        else:
            exit()
