class Revenue():

    # Initializes a revenue problem given a price and quantity
    def __init__(self, name, solving, input1, input2):
        self.name = name

        # input 1 price input 2 quantity
        if solving == "revenue":
            self.price = input1
            self.quantity = input2
            self.revenue = input1 * input2
        # input 1 quantity input 2 revenue
        elif solving == "price":
            self.price = input2 / input1
            self.quantity = input1
            self.revenue = input2
        # input 1 price input 2 revenue
        elif solving == "quantity":
            self.price = input1
            self.quantity = input2 / input1
            self.revenue = input2
        # invalid solve makes empty equation
        else:
            self.price = 0
            self.quantity = 0
            self.revenue = 0

    # returns the string representation of the basic equation
    def getEquation(self):
        return "Revenue = Price * Quantity"
    
    # Returns the full equation represented by the current object
    def getFilledEquation(self):
        return "{:.2f} = {:.2f} * {:.2f}".format(self.revenue, self.price, self.quantity)
    
    def getName(self):
        return self.name
    
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