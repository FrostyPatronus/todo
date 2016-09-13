# --------------------------------
# Makes the file
# --------------------------------

import sys

import glob
from os import walk
from os import remove

sys.path.append("./helper")

import constants as c

# --------------------------------
# Returns the file object
# --------------------------------

def create (curDate):
    return open(c.DIR_TEMP + curDate, "a+")    

# --------------------------------
# Creates file if not exists, deletes
# old file if made in a different day
# --------------------------------

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


