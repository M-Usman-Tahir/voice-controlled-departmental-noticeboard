from Cre import *
from SysPaths import *
import os
from Authentication.OpenFile import *
from Speech import *

def FunList(List):
    """[Takes list and prints it vertically assigning each item its index number on CLI]

    Args:
        List ([string]): [The items to be displayed]

    Returns:
        [string]: [a string displaying entries vertically with its indexes]
    """
    rtnList = "\n"
    for i in range(len(List)):
        rtnList += f"{i+1} - {List[i]}\n"
    return rtnList

def getNum(text):
    """[Takes in the text and return the number in it.]

    Args:
        text ([string]): [text from which an int is to be taken]

    Returns:
        [int]: [smallest number found in the text]
    """
    for i in numbers:
        if f"{i}" in text:
            print(i)
            return numbers[i]
    print(text)
    return "Not found"


def LogIN(name, password=None, found=True):
    """[check the credentials and sends back the path and list of notifications of the user]

    Args:
        name ([string]): [Name or user name of the user]
        password ([string], optional): [password of the user if he is trying to login through credentials]. Defaults to None.
        found (bool, optional): [if he logs in through face detection then it will be true otherwise password will be needed]. Defaults to True.

    Returns:
        [string]: [the path of user's data storage]
        [list]: [list of notifications in the user's account]
    """
    if "CE" in name:
        path = os.path.join(
            StudentPath, "Session-{}".format(name.split("-")[0]), name)
    else:
        path = os.path.join(FacultyPath, name)
    dirs = os.listdir(path)
    if not found:
        with open(os.path.join(path, "CREs.txt"), "r") as data:
            Data = data.read().split("\n")[3].split(": ")[1]
            Password = DC(Data)
            if password == Password:
                return path, dirs
            else:
                say("Invalid Credentials. Please try again.")
                print("Invalid Credentials. Please try again.")
                return False
    else:
        return path, dirs


def Open_Noti(path, dirs):
    """[It shows the dirs in CLI with indexes and then the user chooses the number to open it]

    Args:
        path ([string]): [the path of user's data storage]
        dirs ([list]): [list of notifications in the user's account]
    """
    if len(dirs) > 0:
        while True:
            print(FunList(dirs))
            print("Say the Number of notification to see: ")
            try:
                say("Say the number to open the notification!")
                TEXT = speak()
                print(TEXT)
                N = getNum(TEXT)
                print(N)
                if N == "Not found":
                    say("Couldn't get any number. Please say some number")
                if N == 0:
                    break
                else:
                    OPEN(os.path.join(path, dirs[N-1]))
            except Exception as e:
                print(e)
                # say(e)
                say("Please say that again...")
    else:
        print("There are no notifications yet.")
        say("There are no notifications yet.")


numbers = {"zero": 0,
           "back": 0,
           "one": 1,
           "two": 2,
           "to": 2,
           "too": 2,
           "three": 3,
           "four": 4,
           "five": 5,
           "six": 6,
           "seven": 7,
           "eight": 8,
           "nine": 9,
           0: 0,
           1: 1,
           2: 2,
           3: 3,
           4: 4,
           5: 5,
           6: 6,
           7: 7,
           8: 8,
           9: 9}


if __name__ == '__main__':
    LogIN("2019-CE-34")
