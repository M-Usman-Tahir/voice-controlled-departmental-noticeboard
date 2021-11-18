import sys

from textToSpeech import * # imports speech_recognition as sr
from BOOT import * # imports pandas as pd, os, PasswordGenerator

sys.path.insert(1, os.path.join(sys.path[0], "Mails"))

from BootMails import * # imports SendmMails
