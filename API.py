"""[Node for all modules,
    Takes all funstions here for the main file]
"""

from SetNoti import *
from Speech import * # imports speech_recognition as sr
from BOOT import * # imports pandas as pd, os, PasswordGenerator
from Mails.BootMails import * # imports SendmMails
from Authentication.FaceDetection import * # import SysPaths

f"""
{detectFace()}
"""