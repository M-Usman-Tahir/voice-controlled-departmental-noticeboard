import sys

from textToSpeech import * # imports speech_recognition
from BOOT import * # imports pandas, os, PasswordGenerator

sys.path.insert(1, os.path.join(sys.path[0], "Mails"))

from BootMails import * # imports SendmMails
