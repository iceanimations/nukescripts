@echo off
setlocal
set PYTHONPATH=%VIRTUAL_ENV%\Lib\site-packages
"%NUKE_LOCATION%\python" %*
