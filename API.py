"""[Node for all modules,
    Takes all funstions here for the main file]
"""

from SetNoti import *
from Speech import * # imports speech_recognition as sr
from BOOT import * # imports pandas as pd, os, PasswordGenerator
from Mails.BootMails import * # imports SendmMails
from Authentication.FaceDetection import * # import SysPaths
from Commands import *

"""
Every Functions can be called in the API File.
Simply import the API by `from API import *` and 
use all the functions in that file/module.
"""