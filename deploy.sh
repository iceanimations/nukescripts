#!/bin/bash
dpath=${1%/}

if test -z $dpath; then
    >&2 echo "Error: Must provide a deployment path"
    exit 1
fi

echo "attempting to make the directory: $dpath"
mkdir -p $dpath

echo "deploying at ... $dpath"

venv_path=$VIRTUAL_ENV

if [ "$OS" == "Windows_NT" ]; then
    venv_path=$(cygpath $VIRTUAL_ENV)
fi

echo "copying Qt.py to $dpath..."
cp $venv_path/Lib/site-packages/Qt.py $dpath


myfiles=(\
    createNukeMenu.py\
    ice_init.py\
    ice_menu.py\
    nukeMenuCommands.py\
)

echo copying main files ...
for i in "${myfiles[@]}"
do
    echo "copying $i to $dpath ..."
    cp $i $dpath
done

deploy_submodule() {
    echo "deploying submodule $sm_path to $1 ..."
    rm -rf "$1/$sm_path"
    cp -R $toplevel/$sm_path $1
    return 0
}

export -f deploy_submodule

echo re-generating init.py and menu.py
rm -f $dpath/init.py
rm -f $dpath/menu.py

ppath=$dpath
if [ "$OS" == "Windows_NT" ]; then
    ppath=$(cygpath -w $dpath)
fi

echo "
import site
site.addsitedir(r'${ppath}')
try:
    import ice_init
except ImportError:
    pass" > $dpath/init.py

echo "
import traceback
try:
    import ice_menu
except ImportError:
    traceback.print_exc()" > $dpath/menu.py

git submodule foreach deploy_submodule $dpath
