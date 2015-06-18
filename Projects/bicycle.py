class Bicycle(object):
    def __init__(self, model_name, bike_weight, build_cost):
        self.model_name = model_name
        self.bike_weight = bike_weight
        self.build_cost = build_cost


class BikeShop(Bicycle):
    def __init__(self, shop_name, inventory, margin, profit):
        self.shop_name = "Freddy's Bicycle"
        self.inventory = inventory
        self.margin = .2
        self.profit = (self.build_cost + self.margin) - self.margin


class Customer(object):
    def __init__(self, name, fund, own):
        self.name = name
        self.fund = fund
        self.own = own

# Psuedocode
'''
if __name__ == '__main__':
    create a bike shop with 6 different bike models in stock. The shop should charge its customers 20% over the cost of the bikes.

    create three customers: one has a budget of $200, the second $500 and the third $1000.

    print the name of each customer and list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in a way that each customer can afford at least one.

    print the initial invesntory of the bike shop for each bike it carries

    Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.

    After each customer has purchased their bike, the script should print out the bicycle shops remaining inventory for each bike, and how much profit they have made selling the three bikes.
'''
