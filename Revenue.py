import MicroProblem

class Revenue(MicroProblem):

    # Initializes an empty revenue problem
    def __init__(self):
        self.price = 0
        self.quantity = 0
        self.revenue = 0

    # Initializes a revenue problem given a price and quantity
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
        self.revenue = price * quantity

    # returns the string representation of the basic equation
    def getEquation(self):
        return "Revenue = Price * Quantity"
    
    # Returns the full equation represented by the current object
    def getFilledEquation(self):
        return "{:.2f} = {:.2f} * {:.2f}".format(self.revenue, self.price, self.quantity)
    
    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def getRevenue(self):
        return self.revenue

    def changePrice(self, newPrice):
        self.price = newPrice

    def changeQuantity(self, newQuantity):
        self.quantity = newQuantity

    def clear(self):
        self.price = 0
        self.quantity = 0
        self.revenue = 0