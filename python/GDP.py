class GDP:

    # Initializes GDP Problem with given inputs and a component to solve for
    def __init__(self, name, solving, input1, input2, input3, input4):
        self.name = name

        # input1 investment input2 government input3 net exports input4 gdp 
        if solving == "c":
            self.consumption = input4 - input1 - input2 - input3
            self.investment = input1
            self.government = input2
            self.netExports = input3
            self.gdp = input4
        # input1 consumption input2 government input3 net exports input4 gdp 
        elif solving == "i":
            self.consumption = input1
            self.investment = input4 - input1 - input2 - input3
            self.government = input2
            self.netExports = input3
            self.gdp = input4
        # input1 consumption input2 investment input3 net exports input4 gdp 
        elif solving == "g":
            self.consumption = input1
            self.investment = input2
            self.government = input4 - input1 - input2 - input3
            self.netExports = input3
            self.gdp = input4
        # input1 consumption input2 investment input3 government input4 gdp 
        elif solving == "nx":
            self.consumption = input1
            self.investment = input2
            self.government = input3
            self.netExports = input4 - input1 - input2 - input3
            self.gdp = input4
        # input1 consumption input2 investment input3 government input4 net exports
        elif solving == "gdp":
            self.consumption = input1
            self.investment = input2
            self.government = input3
            self.netExports = input4
            self.gdp = input1 + input2 + input3 + input4
        # invalid solve makes empty equation
        else:
            self.consumption = 0
            self.investment = 0
            self.government = 0
            self.netExports = 0
            self.gdp = 0