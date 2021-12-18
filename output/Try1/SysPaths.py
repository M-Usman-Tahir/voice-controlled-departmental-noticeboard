"""[Gives path to the system for the modules
    to import other modules or files efficiently]
"""

import sys
import os

# sys.path.insert(1, os.path.join(sys.path[0], "Mails"))
# sys.path.insert(1, os.path.join(sys.path[0], "Authentication"))
MainDirPath = sys.path[0]
AuthPath = os.path.join(sys.path[0], "Authentication")
TemplatesPath = os.path.join(sys.path[0], "templates")
LocalPath = os.path.join(sys.path[0], "LOCAL")
PublicPath = os.path.join(LocalPath, "Department-Public")
FacultyPath = os.path.join(LocalPath, "Faculty")
StudentPath = os.path.join(LocalPath, "Student")
OpportunityPath = os.path.join(LocalPath, "Opportunities")
DepartmentPath = os.path.join(PublicPath, "Department")
SocietyPath = os.path.join(PublicPath, "Societies")
