class printer:
    def __init__(self):
        self.__init__ = True

    def dict(data):
        for key, value in data.items():
            print(f"{key}: ${value}")

    ## star allows for non-loop printing
    def listLine(data):
        print(*data)
    
    def listComma(data):
        print(*data, sep=", ")
    
    def listNewLine(data):
        print(*data, sep="\n")

    def raw(data):
        print(data)
