import os
import sys
import logging


nuke_dir = os.path.join(os.path.expanduser('~'), '.nuke')
log_path = os.path.join(nuke_dir, 'startuplog.txt')

__dir__ = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, __dir__)

sys.path.append('r:/Python_Scripts/Nuke')
sys.path.append('r:/Python_Scripts/plugins')
sys.path.append('r:/Python_Scripts/plugins/utilities')
sys.path.append('r:/Python_Scripts/maya2014/PyQt')

try:
    import sip
    sip.setapi('QString', 2)
except ImportError:
    pass

import startup
startup.setupNuke()
