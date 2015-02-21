class Bicycle(object):
    # Define a bike object that has a model, weight and cost attributes
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost


class Shop(object):
    # Define bike shop that has a name, inventory and profit attributes
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.profit = 0

    def sell(self, bicycle):
        # Sell method for bike shop with profit margin on each bike sale
        self.inventory.remove(bicycle)
        margin = (bicycle.cost * 1.2) - bicycle.cost
        self.profit += margin
        return margin

class Customer(object):
    # Define a customer who has a name and who has a fund of dollars
    # to buy a bike. If no value for fund is supplied, set to $500
    def __init__(self, name, fund):
        self.name = name
        self.ride = None # Customers initial ride is none
        self.fund = fund if fund is not None else 500



bike1 = Bicycle("Reid", 10, 500)
print bike1.model
print bike1.weight
print bike1.cost
shop1 = Shop("Reid Cycles")
print shop1.name
print shop1.inventory
print shop1.profit
shop1.inventory.append(bike1)
print shop1.inventory
shop1.sell(bike1)
print shop1.profit
jake = Customer("Jake", 900)
print jake.name
print jake.ride
print jake.fund