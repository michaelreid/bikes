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
    # Define a customer who has a name and who has a budget of dollars
    # to buy a bike. If no value for budget is supplied, set to $500
    def __init__(self, name, budget):
        self.name = name
        self.ride = None # Customers initial ride is none
        self.budget = budget if budget is not None else 500



# Create 1 shop
shop1 = Shop("Reid Cycles")

# Create 6 different bikes and add to the shop's inventory
bike1 = Bicycle("Black Racer 200F", 10, 100)
shop1.inventory.append(bike1)
bike2 = Bicycle("Black Racer 250G", 8, 400)
shop1.inventory.append(bike2)
bike3 = Bicycle("Black Racer 370X", 7.75, 700)
shop1.inventory.append(bike3)
bike4 = Bicycle("Black Mountain Bike 500C", 12, 300)
shop1.inventory.append(bike4)
bike5 = Bicycle("Black Mountain Bike 700B", 11, 400)
shop1.inventory.append(bike5)
bike6 = Bicycle("Black Mountain Bike 900A", 10, 800)
shop1.inventory.append(bike6)

# Create 3 customers with 3 different budgets
jake = Customer("Jake", 200)
john = Customer("John", 500)
jeff = Customer("Jeff", 1000)

# Loop through inventory
def bikes_in_budget(customer, shop):
    # print customer's name
    print customer.name
    # create a list of bikes within the customer's budget
    can_afford = []
    # loop through the shop's inventory and check if
    # customer can afford the bikes
    for bikes in shop.inventory:
        if (bikes.cost * 1.2) < customer.budget:
            can_afford.append(bikes.model)
    # print a list of the bikes within the customer's budget     
    print can_afford

bikes_in_budget(jake, shop1)
bikes_in_budget(john, shop1)
bikes_in_budget(jeff, shop1)
    
        