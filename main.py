# Bicycle Industry Model as part of Thinkful course
#
# Bicycle industry refactored.
# Classes separated into own file: bikes.py
#
# February 2015 version 2.0


# TODO: make the main.py file import the classes from the bicycles.py file
# STUCK AT THIS POINT
# TRIED:
# import bicycles
#
# import Customer etc.
#
from bikes import *

# Create 1 bicycle shop
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

# Print out the initial inventory of the bike shop
def print_inventory(shop):
    # Initially print the name of the shop
    print 'List of ' + shop.name + ' inventory:'
    # Print the model, weight and cost of the bikes in inventory
    for bike in shop.inventory:
        # TODO: How do I make the next line not be so long, but print on one line
        print 'model: ' + bike.model + ' weight: ' + str(bike.weight) + 'kg ' + 'cost: $' + str(bike.cost) 

        
# Create 3 customers with 3 different budgets
jake = Customer("Jake", 200)
john = Customer("John", 500)
jeff = Customer("Jeff", 1000)

# Print the bikes within a customer's budget
def bikes_in_budget(customer, shop):
    # print customer's name
    print 'Customer Name is: ' + customer.name
    print 'Customer Budget is: $' + str(customer.budget)
    # loop through the shop's inventory and check if
    # customer can afford the bikes
    print 'Customer can buy:'
    for bike in shop.inventory:
        bike_retail_price = bike.cost * 1.2
        if bike_retail_price < customer.budget:
            print bike.model + ' - RRP $' + str(bike_retail_price)


# Print the initial inventory of the shop
print_inventory(shop1)
print ""


# Determine which bikes are in customer's budget            
bikes_in_budget(jake, shop1)
print ""
bikes_in_budget(john, shop1)
print ""
bikes_in_budget(jeff, shop1)
print ""
print ""

# Customers each buy a bike
jake.purchase(bike1)
shop1.sell(bike1)
print ""
john.purchase(bike5)
shop1.sell(bike5)
print ""
jeff.purchase(bike3)
shop1.sell(bike3)
print ""

# Print out the shop's remaining inventory and profit
print_inventory(shop1)
print ""
print shop1.name + ' profit from sales is: $' + str(shop1.profit)