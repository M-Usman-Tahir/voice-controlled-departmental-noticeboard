"""[Gives path to the system for the modules
    to import other modules or files efficiently]
"""

import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], "Mails"))
sys.path.insert(1, os.path.join(sys.path[0], "Authentication"))
AuthPath = sys.path[1]
MainDirPath = sys.path[0]
TemplatesPath = os.path.join(sys.path[0], "templates")
LocalPath = os.path.join(sys.path[0], "LOCAL")
PublicPath = os.path.join(LocalPath, "Department-Public")
DepartmentPath = os.path.join(PublicPath, "Department")
SocietyPath = os.path.join(PublicPath, "Societies")
OpportunityPath = os.path.join(LocalPath, "Opportunities")
FacultyPath = os.path.join(LocalPath, "Faculty")
StudentPath = os.path.join(LocalPath, "Student")
