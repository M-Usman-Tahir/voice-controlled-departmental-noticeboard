import os
# from posixpath import split
import sys
from BOOT import listMails
from Mails.SendPDF import *
from Mails.BootMails import *


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

def GetPath(path = os.path.join(sys.path[0], "LOCAL")):
    """[Walk through directories and return the list of sub-directories]

    Args:
        path ([string], optional): [path of directory to start walking through]. Defaults to the path of storage.

    Returns:
        [string]: [path of internally selected directory unless it finds credentials file or the zero is entered as input.]
    """
    try:
        dirs = os.listdir(path)
        if "CREs.txt" in dirs or len(dirs)==0:
            return path
        print(FunList(dirs))
        c = int(input("Enter the Dir num: "))
        if c == 0:
            return path
        return GetPath(os.path.join(path, dirs[c-1]))
    except Exception as e:
        print(e)
        return path
    
def AskNoti():
    """[To replace the notification from one folder to the storage and send the email to the respective members.]
    """
    C_Noti = input("Enter the path of the notification: ")
    if not os.path.exists(C_Noti):
        print("Path doesnot exists...")
        return
    T_Path = os.path.join(GetPath(), os.path.split(C_Noti)[1])
    if not "Student" in T_Path:
        sendPDFMail("A new notification has been added.", C_Noti, subject="A new notification", recievers=listMails)
    else:
        with open(os.path.join(T_Path, "CREs.txt"), "r") as f:
            R = DC(f.read()).split("\n")[2].split(": ")[1].strip()
        sendPDFMail("A new notification has been added.", C_Noti, subject="A new notification", recievers=[R])
    os.replace(C_Noti, T_Path)
    # ! sendMailNoti(T_path)
def AdminLog():
    Pass = PasswordGenerator()
    SendBootCre(Pass, Topic="admin")
    if input("Enter the password sent you through mail: ") == Pass:
        AskNoti()
    else:
        print("Wrong Credentials...")
    
if __name__ == '__main__':
    AskNoti()