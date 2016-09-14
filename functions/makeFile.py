# --------------------------------
# Makes the file
# --------------------------------

from os import walk
from os import remove

import constants as c

file = None

# --------------------------------
# Returns the file object
# --------------------------------

def create (curDate):
    global file
    file = open(c.DIR_TEMP + curDate, "a+")   
    return  file

# --------------------------------
# Creates file if not exists, deletes
# old file if made in a different day
# --------------------------------

def createFile(curDate):
    pastDate = None
    for (dirpath, dirnames, filenames) in walk(c.DIR_TEMP):
        pastDate = filenames[0]
        break

    if pastDate != curDate:
        remove(c.DIR_TEMP + pastDate)

    return create(curDate)