import sys
sys.path.append("./functions")
import makeFile
import interactive as i


def switch(command, data):
    print command
    return {
        
        "-i": i.interactive
        "add": 

    }.get(command)(command, data)

