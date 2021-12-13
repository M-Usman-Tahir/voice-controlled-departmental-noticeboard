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

def AskCRE():
    say("Please enter your login credentails")
    name = input("Enter your Name: ")
    Pass = input("Enter your password: ")
    return name.upper(), Pass
    

def Command(text):
    if IfIn(["log", "in"], text, "and") or "scan" in text:
        name = detectFace()
        if name != "Not Found":
            try:
                path, ListDirs = LogIN(name)
            except Exception as e:
                say(e)
                print(e)
                return
        else:
            say("No matching face detected!")
            name, Pass = AskCRE()
            path, ListDirs = LogIN(name, Pass, False)
        ListDirs.remove("CREs.txt")
        Open_Noti(path, ListDirs)
    if IfIn(["opportunity", "opportunities"], text):
        dirs = os.listdir(OpportunityPath)
        print(FunList(dirs))
        say("Say the number of notification to open")
        TEXT = speak()
        N=getNum(TEXT)
        OPEN(os.path.join(OpportunityPath, dirs[N-1]))
    if IfIn(["public", "department"], text):
        dirs = os.listdir(DepartmentPath)
        print(FunList(dirs))
        say("Say the number of notification to open")
        TEXT = speak()
        N=getNum(TEXT)
        OPEN(os.path.join(DepartmentPath, dirs[N-1]))
    if IfIn(["society", "societies"], text):
        dirs = os.listdir(SocietyPath)
        print(FunList(dirs))
        say("Say the number of notification to open")
        TEXT = speak()
        N=getNum(TEXT)
        OPEN(os.path.join(SocietyPath, dirs[N-1]))
        