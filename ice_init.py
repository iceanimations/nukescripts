import os
import sys
import nuke

__dir__ = os.path.abspath(os.path.dirname(__file__))

if nuke.NUKE_VERSION_MAJOR < 9:
    os.environ['QT_PREFERRED_BINDING'] = 'PyQt4'

sys.path.insert(0, __dir__)
sys.path.append('r:/Python_Scripts/Nuke')
sys.path.append('r:/Python_Scripts/plugins')
sys.path.append('r:/Python_Scripts/plugins/utilities')
sys.path.append('r:/Python_Scripts/maya2014/PyQt')

import startup
startup.setupNuke()
