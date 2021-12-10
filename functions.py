"""[Node for all modules,
    Takes all funstions here for the main file]
"""

from SysPaths import *
from SetNoti import *
from Speech import * # imports speech_recognition as sr
from BOOT import * # imports pandas as pd, os, PasswordGenerator
from BootMails import * # imports SendmMails
from Login import *
from OpenFile import *
from FaceDetection import * # import SysPaths


def Command(text):
    if IfIn(["log", "in"], text, "and") or "scan" in text:
        name = detectFace()
        if name != "Not Found":
            LogIN(name)
        else:
            say("No matching face detected!")
    if IfIn(["opportunity", "opportunities"], text):
        dirs = os.listdir(OpportunityPath)
        print(FunList(dirs))
        say("Say the number of notification to open")
        TEXT = speak(engine)
        N=getNum(TEXT)
        OPEN(os.path.join(OpportunityPath, dirs[N-1]))
    if IfIn(["public", "department"], text):
        dirs = os.listdir(DepartmentPath)
        print(FunList(dirs))
        say("Say the number of notification to open")
        TEXT = speak(engine)
        N=getNum(TEXT)
        OPEN(os.path.join(DepartmentPath, dirs[N-1]))
    if IfIn(["society", "societies"], text):
        dirs = os.listdir(SocietyPath)
        print(FunList(dirs))
        say("Say the number of notification to open")
        TEXT = speak(engine)
        N=getNum(TEXT)
        OPEN(os.path.join(SocietyPath, dirs[N-1]))
        