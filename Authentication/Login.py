# import os
# CurrentDir = os.getcwd()
# print(CurrentDir)

import SysPaths as SP
import os
from OpenFile import *

def FunList(List):
    rtnList = "\n"
    for i in range(len(List)):
        rtnList += f"{i+1} - {List[i]}\n"
    return rtnList

def LogIN(name):
    if "CE" in name:
        path = os.path.join(SP.StudentPath, "Session-{}".format(name.split("-")[0]), name)
        dirs = os.listdir(path)
        dirs.remove("CREs.txt")
        if len(dirs)>0:
            print(FunList(dirs))
            N = int(input("Enter the Number of notification to see: "))
            OPEN(os.path.join(path, dirs[N-1]))
        else:
            print("There are no notifications yet.")
            
def logout():
    pass

if __name__ == '__main__':
    LogIN("2019-CE-34")
