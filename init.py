import pandas as pd
import os

CurrentDir = os.getcwd()

os.chdir(os.path.join(os.getcwd(), "Student-Details"))

for root, dirs, files in os.walk(os.getcwd()):
    for name in files:
        file1 = pd.read_csv(name)
        NewPath = os.path.join(CurrentDir, "LOCAL", "Students", "Session-{}".format(file1["Reg_No"].iloc[2].split("-")[0]))
        try:
            os.mkdir(NewPath)
        except FileExistsError:
            continue
        for i in file1["Reg_No"]:
            try:
                os.mkdir(os.path.join(NewPath, i))
            except:
                pass
            with open("{}.txt".format(os.path.join(NewPath, i, "CREs")), "w") as Cre:
                Cre.write("Name: {}".format(file1[file1["Reg_No"]==i]["Name"]))
                            
    break