import os
import site

__dir__ = os.path.dirname(__file__)
site.addsitedir(__dir__)

import createNukeMenu
createNukeMenu.create()
