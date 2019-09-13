import os
import site
import sys

__dir__ = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, __dir__)

sys.path.append('r:/Python_Scripts/plugins')
sys.path.append('r:/Python_Scripts/plugins/utilities')
sys.path.append('r:/Python_Scripts/maya2014/PyQt')

import createNukeMenu
createNukeMenu.create()
