from SendMails import *
from SysPaths import TemplatesPath
import os

def SendBootCre(data, rec=None, Topic="Student"):
    Data = data.split('\n')
    # print(Data)
    if Topic=="Student":
        Name = " ".join(Data[0].split()[1:])
        Roll = Data[1].split()[1]
        Password = Data[3].split()[1]
    print(Name, Roll, Password)
    with open(os.path.join(TemplatesPath, "Password.html"), "r") as file:
        body = file.read()
        body = Name.join(body.split("[STUDENT]"))
        body = Roll.join(body.split("(20XX-CE-XX)"))
        body = Password.join(body.split("[GENERATED PASSWORD]"))
    
    body = (body, "html")
    sendMail(body, subject="Account Created", recievers=[rec])
