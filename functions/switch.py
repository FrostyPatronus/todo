import sys
sys.path.append("./functions")
import makeFile
import interactive as i


def switch(command, data):
    print command
    return {
        
        "-i": lambda: i.interactive()

    }.get(command)()

