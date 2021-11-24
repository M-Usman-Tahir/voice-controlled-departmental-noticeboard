"""[Gives path to the system for the modules
    to import other modules or files efficiently]
"""

import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], "Mails"))
sys.path.insert(1, os.path.join(sys.path[0], "Authentication"))
MainDirPath = sys.path[0]
TemplatesPath = os.path.join(sys.path[0], "templates")
PublicPath = os.path.join(sys.path[0], "LOCAL", "Department-Public")
OpportunityPath = os.path.join(sys.path[0], "LOCAL", "Opportunities")
FacultyPath = os.path.join(sys.path[0], "LOCAL", "Faculty")
StudentPath = os.path.join(sys.path[0], "LOCAL", "Student")
