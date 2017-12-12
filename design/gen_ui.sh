#!/bin/bash
# This script generate the .py files
# from qt .ui files


function ui {
    pyuic5.exe $1.ui -o $1.py
}


for file in `ls *.ui`
do

    ui ${file%.ui}
    echo "Regenerated for ${file} -> ${file%.ui}.py"
done
