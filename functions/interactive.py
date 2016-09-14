cdimport switch 
def interactive(data=None):
    while True:
        raw = raw_input(">>> ")
        raw = raw.split(" ", 1)
        command = raw[0]
        data = raw[1]

        switch.switch(command, data)