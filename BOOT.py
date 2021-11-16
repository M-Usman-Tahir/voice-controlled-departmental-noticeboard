import pandas as pd
import os
from Cre import PasswordGenerator


def StructureBoot():
    CurrentDir = os.getcwd()
    os.chdir(os.path.join(os.getcwd(), "Student-Details"))

    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            file1 = pd.read_csv(name)
            NewPath = os.path.join(CurrentDir, "LOCAL", "Students", "Session-{}".format(file1["Reg_No"].iloc[2].split("-")[0]))
            try:
                os.mkdir(NewPath)
            except FileExistsError:
                pass
            for i in file1["Reg_No"]:
                try:
                    os.mkdir(os.path.join(NewPath, i))
                except:
                    pass
                try:
                    Name = list(file1[file1["Reg_No"]==i]["Name"])[0]
                    RollNum = i
                    Email = list(file1[file1["Reg_No"]==i]["Email"])[0]
                    Password = PasswordGenerator()
                    with open("{}.txt".format(os.path.join(NewPath, i, "CREs")), "w") as Cre:
                        Data = "Name: {}\nRoll_Number: {}\nEmail: {}\nPasswaord: {}\n".format(Name, RollNum, Email, Password)
                        Cre.write(Data)
                        # ! SendMail(Data)
                except:
                    print(i)                 
        break
    os.chdir(CurrentDir)

def Boot():
    path = os.path.join(os.getcwd(), "LOCAL")
    Paths = [["Students"],
            ["Opportunities"],
            ["Faculty"],
            ["Department-Public", "Societies"], 
            ["Department-Public", "Department"]]
            
    for p in Paths:
        try:
            os.makedirs(os.path.join(path, *p))
        except FileExistsError:
            continue
    StructureBoot()

if __name__ == '__main__':
    Boot()