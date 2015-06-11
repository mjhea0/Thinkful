class bicycle(object)
    def __init__(self, model, weight, cost)
        self.model = model
        self.weight = weight
        self.cost = cost

class bikeShop(bicycle)
    def __init__(self, shop_name, inventory, margin, profit)
        self.shop_name = "Freddy's Bicycle"
        self.inventory = inventory
        self.margin = .2
        self.profit = (self.cost + self.margin) - self.margin
               
class customer(object)
    def __init__(self, name, fund, own)
        self.name = name
        self.fund = fund
        self.own = own
