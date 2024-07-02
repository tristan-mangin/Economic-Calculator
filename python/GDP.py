'''
Created by Tristan Mangin on 6.29.2024

This file will handle the representation of any basic GDP problems.
'''
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
    
    '''
    ACCESSORS
    '''

    # returns the string representation of the basic equation
    def getEquation(self):
        return "GDP = N + I + G + NX"
    
    # Returns the full equation represented by the current object
    def getFilledEquation(self):
        return "{:.2f} = {:.2f} + {:.2f} + {:.2f} + {:.2f}".format(self.gdp, self.consumption, self.investment, self.government, self.netExports)
    
    def getType(self):
        return "GDP Problem"

    def getName(self):
        return self.name
    
    def getConsumption(self):
        return self.consumption
    
    def getInvestment(self):
        return self.investment
    
    def getGovernment(self):
        return self.government
    
    def getNetExport(self):
        return self.netExports

    def getGDP(self):
        return self.gdp
    
    '''
    MODIFIERS
    '''

    def setConsumption(self, c):
        self.gdp = self.gdp - self.consumption + c
        self.consumption = c

    def setInvestment(self, i):
        self.gdp = self.gdp - self.investment + i
        self.investment = i

    def setGovernment(self, g):
        self.gdp = self.gdp - self.government + g
        self.government = g
    
    def setNetExports(self, nx):
        self.gdp = self.gdp - self.netExports + nx
        self.netExports = nx

    def clear(self):
        self.price = 0
        self.quantity = 0
        self.revenue = 0