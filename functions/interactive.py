import switch 
def interactive():
    while True:
        raw = input(">>> ")

        raw = raw.split()
        command = raw[0]
        data = raw[1 : ]

        switch.switch()