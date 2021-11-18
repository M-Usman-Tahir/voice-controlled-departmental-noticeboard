    """[Gives path to the system for the modules
        to import other modules or files efficiently]
    """

import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], "Mails"))
sys.path.insert(1, os.path.join(sys.path[0], "Authentication"))
