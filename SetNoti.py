import os
from SysPaths import *

def FunList(List):
    rtnList = "\n"
    for i in range(len(List)):
        rtnList += f"{i+1} - {List[i]}\n"
    return rtnList

def GetPath(path = LocalPath):
    try:
        dirs = os.listdir(path)
        if "CREs.txt" in dirs or len(dirs)==0:
            return path
        print(FunList(dirs))
        c = int(input("Enter the Dir num: "))
        return GetPath(os.path.join(path, dirs[c-1]))
    except Exception as e:
        print(e)
        return path
    
def AskNoti():
    C_Noti = input("Enter the path of the notification: ")
    T_Path = os.path.join(GetPath(), os.path.split(C_Noti)[1])
    os.replace(C_Noti, T_Path)
    # ! sendMailNoti(T_path)

if __name__ == '__main__':
    AskNoti()