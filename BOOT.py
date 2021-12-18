import pandas as pd
from Cre import *
from Mails.BootMails import *


def StructureBoot(part, check="Reg_No"):
    CurrentDir = os.getcwd()
    os.chdir(os.path.join(os.getcwd(), "Details", part+"-Details"))
    
    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            file1 = pd.read_csv(name)
            NewPath = os.path.join(CurrentDir, "LOCAL", part)
            NewPath = os.path.join(NewPath, "Session-{}".format(file1[check].iloc[0].split("-")[0])) if part=="Student" else NewPath
            try:
                os.mkdir(NewPath)
            except FileExistsError:
                pass
            for i in file1[check]:
                try:
                    os.mkdir(os.path.join(NewPath, i))
                except:
                    pass
                try:
                    if part == "Student":
                        Name = list(file1[file1[check]==i]["Name"])[0]
                        RollNum = i
                        Email = list(file1[file1[check]==i]["Email"])[0]
                        Password = PasswordGenerator()
                        with open("{}.txt".format(os.path.join(NewPath, i, "CREs")), "w") as Cre:
                            Data = "Name: {}\nRoll_Number: {}\nEmail: {}\nPasswaord: {}\n".format(Name, RollNum, Email, Password)
                            Cre.write(DC(Data))
                            os.chdir(CurrentDir)
                            SendBootCre(Data, Email, Topic="Student")
                            os.chdir(NewPath)
                            
                        
                    elif part == "Faculty":
                        Name = i
                        Email = list(file1[file1[check]==i]["Email"])[0]
                        Position = list(file1[file1[check]==i]["Position"])[0]
                        Password = PasswordGenerator()
                        Subjects = list(file1[file1[check]==i]["Subjects"])[0]
                        with open("{}.txt".format(os.path.join(NewPath, i, "CREs")), "w") as Cre:
                            Data = "Name: {}\nPosition: {}\nEmail: {}\nPasswaord: {}\nSubjects: {}\n".format(Name, Position, Email, Password, Subjects)
                            Cre.write(DC(Data))
                            os.chdir(CurrentDir)
                            SendBootCre(Data, Email, Topic="Teacher")
                            os.chdir(NewPath)
                            
                except Exception as e:
                    print(i, e)                 
        break
    os.chdir(CurrentDir)

def Boot():
    path = os.path.join(os.getcwd(), "LOCAL")
    Paths = [["Student"],
            ["Opportunities"],
            ["Faculty"],
            ["Department-Public", "Societies"], 
            ["Department-Public", "Department"]]
            
    for p in Paths:
        try:
            os.makedirs(os.path.join(path, *p))
        except FileExistsError:
            continue
    StructureBoot("Student")
    StructureBoot("Faculty", "Name")
    

if __name__ == '__main__':
    Boot()