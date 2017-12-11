#!/usr/bin/python
# you should have pyinstaller instaled

import os

flags = "--onefile --noconsole --name rentalcar"
fpath = "rentalcar/__main__.py"


os.system("pyinstaller {} {}".format(flags, fpath))
