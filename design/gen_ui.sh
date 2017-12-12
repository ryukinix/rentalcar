#!/bin/bash
# This script generate the .py files
# from qt .ui files

path=../rentalcar/forms

function ui {
    pyuic5 $1.ui -o $path/$1.py
}


for file in `ls *.ui`
do

    ui ${file%.ui}
    echo "Regenerated for ${file} -> $path/${file%.ui}.py"
done

echo "Press enter to close..."
read
