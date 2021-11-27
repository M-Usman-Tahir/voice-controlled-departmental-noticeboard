"""[Gives path to the system for the modules
    to import other modules or files efficiently]
"""

import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], "Mails"))
sys.path.insert(1, os.path.join(sys.path[0], "Authentication"))
MainDirPath = sys.path[0]
TemplatesPath = os.path.join(sys.path[0], "templates")
LocalPath = os.path.join(sys.path[0], "LOCAL")
PublicPath = os.path.join(LocalPath, "Department-Public")
OpportunityPath = os.path.join(LocalPath, "Opportunities")
FacultyPath = os.path.join(LocalPath, "Faculty")
StudentPath = os.path.join(LocalPath, "Student")
