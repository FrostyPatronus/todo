# --------------------------------
# Makes the file
# --------------------------------
import sys

import glob
from os import walk
from os import remove

sys.path.append("./helper")

import constants as c

def create (curDate):
    with open(c.DIR_TEMP + curDate, "a+") as f:
        f.write("ADS<O<DA")
    

def createFile(curDate):
    pastDate = None
    for (dirpath, dirnames, filenames) in walk(c.DIR_TEMP):
        pastDate = filenames[0]
        break

    print pastDate
    print curDate
    if pastDate != curDate:
        remove(c.DIR_TEMP + pastDate)
    
    return create(curDate)


