import speech_recognition as sr
import pyttsx3
from SysPaths import *
from Authentication.OpenFile import *
from Authentication.Login import *
from Authentication.FaceDetection import *

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def say(text):
    """[It narrates up the text and wait until all the text is spoken out.]

    Args:
        text ([string]): [the text to be narrated.]
    """
    engine.say(text)
    engine.runAndWait()

def speak():
    """[It recognizes the speech and converts into the text.
    It takes in the pyttsx3 engine to speak out the errors if encountered.]

    Args:
        engine ([pyttsx3.Engine]): [For the system to speak out the information or alerts]

    Returns:
        [string]: [The text of speech understood by the google API]
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)            
        except sr.UnknownValueError:
            engine.say("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            engine.say("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""
        except Exception as e:
            engine.say("Oooops, an error occurred: ")
            engine.say(str(e))
            print(e)
            return ""
        finally:
            engine.runAndWait()
            
def IfIn(words, text, opr="or"):
    """[It take a array of words and checks if the words are present in the text
    and return their AND or OR relation mentioned in the arguments.]

    Args:
        words ([list of strings]): [The words to check if present in text]
        text ([string]): [The simple string text]
        opr (str, optional): [The logical realtion of booleans i.e. AND, OR]. Defaults to "or".

    Returns:
        [boolean]: [The relation of 'opr' with all the boolean of matches (word in text)]
    """
    if opr=="or":
        for word in words:
            if word in text:
                return True
        return False
    for word in words:
        if word in text:
            continue
        return False
    return True


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
        