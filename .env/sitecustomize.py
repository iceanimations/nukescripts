from __future__ import print_function

import os
import site

_nuke_ver = os.environ.get("NUKE_VERSION")
_n_loc = os.environ.get("NUKE_LOCATION")

os.environ["PYTHONHOME"] = (_n_loc)
os.environ["Path"] = _n_loc+";" + os.environ["Path"]
os.environ["QT_PLUGIN_PATH"] = _n_loc+"/qtplugins"

site.addsitedir(_n_loc+"/lib/site-packages")
site.addsitedir(_n_loc+"/DLLs")
site.addsitedir(_n_loc+"/lib")
site.addsitedir(_n_loc+"/lib/plat-win")
site.addsitedir(_n_loc+"/lib/lib-tk")
site.addsitedir(_n_loc)
site.addsitedir(os.path.abspath('.'))
site.addsitedir('.')
