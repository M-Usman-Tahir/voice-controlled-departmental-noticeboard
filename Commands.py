from Authentication.Login import *
from Authentication.FaceDetection import *
           
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

def AskCRE(window=""):
    say("Enter your credentials")
    print("Enter your credentials")
    # window.loginWindow()
    name = input("Enter your Name: ")
    Pass = input("Enter your password: ")
    return name.upper(), Pass
    

def Command(text, window=""):
    if IfIn(["log", "in"], text, "and") or "scan" in text:
        name = detectFace()
        if name != "Not Found":
            try:
                path, ListDirs = LogIN(name)
                Loggedin(name)
            except Exception as e:
                say(e)
                print(e)
                return
        else:
            say("Facial Recognition failed...")
            name, Pass = AskCRE(window)
            try:
                path, ListDirs = LogIN(name, Pass, False)
                Loggedin(name)
            except:
                say("Ooopss, it seems you forgot your password.")
                print("Ooopss, it seems you forgot your password.")
        ListDirs.remove("CREs.txt")
        Open_Noti(path, ListDirs)
    if IfIn(["opportunity", "opportunities"], text):
        # window.opportunitiesWindow()
        dirs = os.listdir(OpportunityPath)
        if not dirs:
            say('No Notification found regarding opportunities')
        else:
            print(FunList(dirs))
            say("Say the number of notification to open")
            TEXT = speak()
            N=getNum(TEXT)
            OPEN(os.path.join(OpportunityPath, dirs[N-1]))
    if IfIn(["public", "department", "departmental","notification"], text):
        # window.notificationWindow()
        dirs = os.listdir(DepartmentPath)
        if not dirs:
            say('No Public Notification found')
        else:
            print(FunList(dirs))
            say("Say the number of notification to open")
            TEXT = speak()
            N=getNum(TEXT)
            OPEN(os.path.join(DepartmentPath, dirs[N-1]))
    if IfIn(["society", "societies"], text):
            # window.eventsWindow()
            dirs = os.listdir(SocietyPath)
            if not dirs:
                say('No Updates regarding societies')
            else:
                print(FunList(dirs))
                say("Say the number of notification to open")
                TEXT = speak()
                N=getNum(TEXT)
                OPEN(os.path.join(SocietyPath, dirs[N-1]))
            