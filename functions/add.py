# --------------------------------
# Adds the todo in the file
# --------------------------------
import makeFile as m

def add(lines):
    file = m.file

    for line in lines:
        file.write(line + "\n")
