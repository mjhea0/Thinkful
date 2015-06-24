class Bicycle(object):
    def __init__(self, model_name, bike_weight, bike_cost):
        self.model_name = model_name
        self.bike_weight = bike_weight
        self.bike_cost = bike_cost


class BikeShop(Bicycle):
    def __init__(self, shop_name, inventory):
        self.shop_name = shop_name
        self.inventory = inventory
        self.profit = 0

    def getShopName(self):
        return self.shop_name

    def getInventory(self):
        for bikes in self.inventory:
            return bikes


class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.own_bike = None


if __name__ == '__main__':

# bike models for inventory
    hybrid = Bicycle("hybrid", 20, 400)
    bmx = Bicycle("bmx", 10, 80)
    road = Bicycle("road", 15, 560)
    mountain = Bicycle("mountain", 30, 320)
    racing = Bicycle("racing", 10, 640)
    cruiser = Bicycle("cruiser", 40, 160)

    initial_inventory = [hybrid, bmx, road, mountain, racing, cruiser]

    shop = BikeShop("Freddys Bicycles", initial_inventory)

# customers
    josh = Customer("Josh", 1000)
    john = Customer("John", 500)
    joan = Customer("Joan", 200)

    customersList = [josh, john, joan]

    print "Welcome to {}!".format(shop.getShopName())

#    for buyer in customerList:
#      if bike price <=  buyer.budget:
#           print "Here are the bikes within your budget: ".format(bike)
#      choose one bike and make it = customer.own_bike
#      print "{0} just purchased {1} at {2} and have {3} left over".format(customer, bike price, remaining budget)

