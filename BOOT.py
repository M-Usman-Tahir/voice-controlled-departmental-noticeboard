import os

path = os.path.join(os.getcwd(), "LOCAL")
Paths = [["Students", "Opportunities"],
        ["Faculty"],
        ["Department-Public", "Societies"], 
        ["Department-Public", "Department"]]
        
for p in Paths:
    try:
        os.makedirs(
            os.path.join(path, *p)
        )
    except FileExistsError:
        continue