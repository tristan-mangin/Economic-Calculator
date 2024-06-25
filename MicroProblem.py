class MicroProblem:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Micro: {}".format(self.name)

    def printName(self):
        print(self.name)