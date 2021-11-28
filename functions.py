"""[Node for all modules,
    Takes all funstions here for the main file]
"""

# from Authentication.OpenFile import OPEN
from SetNoti import *
from SysPaths import *
from textToSpeech import * # imports speech_recognition as sr
from BOOT import * # imports pandas as pd, os, PasswordGenerator
from BootMails import * # imports SendmMails
from Login import *
from OpenFile import *
from FaceDetection import *


def Command(engine, text):
    if IfIn(["log", "in"], text, "and") or "scan" in text:
        name = detectFace()
        if name != "Not Found":
            LogIN(name)
        else:
            say(engine, "No matching face detected!")
    if IfIn(["opportunity", "opportunities"], text):
        dirs = os.listdir(OpportunityPath)
        print(FunList(dirs))
        say(engine, "Say the number of notification to open")
        TEXT = speak(engine)
        N=getNum(TEXT)
        OPEN(os.path.join(OpportunityPath, dirs[N-1]))
    if IfIn(["public", "department"], text):
        dirs = os.listdir(DepartmentPath)
        print(FunList(dirs))
        say(engine, "Say the number of notification to open")
        TEXT = speak(engine)
        N=getNum(TEXT)
        OPEN(os.path.join(DepartmentPath, dirs[N-1]))
    if IfIn(["society", "societies"], text):
        dirs = os.listdir(SocietyPath)
        print(FunList(dirs))
        say(engine, "Say the number of notification to open")
        TEXT = speak(engine)
        N=getNum(TEXT)
        OPEN(os.path.join(SocietyPath, dirs[N-1]))
        
    pass
    