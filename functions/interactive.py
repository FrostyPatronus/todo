import switch 
def interactive(data=None):
    print "<<< INTERACTIVE MODE >>>"
    print "Use comma, space to separate arguments"

    while True:
        raw = raw_input(">>> ") + " "
        raw = raw.split(" ", 1)

        command = raw[0]
        data = raw[1].split(", ")

        switch.switch(command, data)