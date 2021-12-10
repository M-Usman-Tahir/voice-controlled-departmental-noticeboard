# import os
# CurrentDir = os.getcwd()
# print(CurrentDir)

import SysPaths as SP
import os
from OpenFile import *
from textToSpeech import *
from init import engine

def FunList(List):
    rtnList = "\n"
    for i in range(len(List)):
        rtnList += f"{i+1} - {List[i]}\n"
    return rtnList

def getNum(text):
    for i in numbers:
        if i in text:
            print(i)
            return numbers[i]
    print(text)
    return text

def LogIN(name):
    if "CE" in name:
        path = os.path.join(SP.StudentPath, "Session-{}".format(name.split("-")[0]), name)
    else:
        path = os.path.join(SP.FacultyPath, name)
    dirs = os.listdir(path)
    dirs.remove("CREs.txt")
    if len(dirs)>0:
        while True:
            print(FunList(dirs))
            print("Enter the Number of notification to see: ")
            try:
                say("Say the number to open the notification!")
                TEXT = speak()
                print(TEXT)
                N=getNum(TEXT)
                print(N)
                if N == 0:
                    break
                OPEN(os.path.join(path, dirs[N-1]))
            except Exception as e:
                print(e)
                say(e)
                say("Please say that again...")
    else:
        print("There are no notifications yet.")
        say("There are no notifications yet.")


numbers = {"one":1,
           "two":2,
           "three":3,
           "four":4,
           "five":5,
           "six":6,
           "seven":7,
           "eight":8,
           "nine":9,
           1:1,
           2:2,
           3:3,
           4:4,
           5:5,
           6:6,
           7:7,
           8:8, 
           9:9}


if __name__ == '__main__':
    LogIN("2019-CE-34")
