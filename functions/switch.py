import makeFile
import interactive as i
import add


def switch(command, data):
    return {

        "-i": i.interactive,
        "add": add.add

    }.get(command)(data)
