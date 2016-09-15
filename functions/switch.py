import makeFile
import interactive as i
import add


def switch(command, data):
    return {

        "-i": i.interactive,
        "add": add.add,
        "quit": quit

    }.get(command)(data)
