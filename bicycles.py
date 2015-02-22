# Model the Bicycle Industry as part of Thinkful course
#
# February 2015
#
# Define classes for Bicycles, Bike Shops & Customers
#
#

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
       

class Customer(object):
    # Define a customer who has a name and who has a budget of dollars
    # to buy a bike. If no value for budget is supplied, set to $500
    def __init__(self, name, budget):
        self.name = name
        self.ride = None # Customers initial ride is none
        self.budget = budget if budget is not None else 500

    def purchase(self, bike):
        print "Customer name is: " + self.name
        retail_price = bike.cost * 1.2
        if retail_price > self.budget:
            print "That bike's too expensive, choose another one."
        else:
            self.ride = bike.model
            self.budget = self.budget - retail_price
            print "Customer " + self.name + " now owns: " + self.ride
            print "Customer " + self.name + " has: $" + str(self.budget) + " left"