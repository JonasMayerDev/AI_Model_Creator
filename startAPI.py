#!/usr/bin/env python3

import sys
import os

os.system("/bin/bash "+sys.path[0]+"/InstallGeneral.bash "+sys.path[0])
os.system("cd "+sys.path[0]+"/QtGUI && python3 "+sys.path[0]+"/QtGUI/controller.py")