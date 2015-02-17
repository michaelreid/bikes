class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost


class Shop(object):
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.profit = 0

    def sell(self, bicycle):
        self.inventory.remove(bicycle)
        margin = (bicycle.cost * 1.2) - bicycle.cost
        self.profit += margin
        return margin




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