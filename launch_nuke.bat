@echo off
setlocal
set "PYTHONPATH=%VIRTUAL_ENV%\Lib\site-packages;%dp0"
start cmd /c "%NUKE_LOCATION%\Nuke%_NUKE_VER_NUM%.exe" %*
