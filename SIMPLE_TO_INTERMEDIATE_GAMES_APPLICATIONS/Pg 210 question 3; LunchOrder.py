##Bansari Shah
##ICS4U-C
##Pg 210 #3; LunchOrder
##04/06/2022


class LunchOrder:

    def __init__(self, h, s, f, so):
        self.cost = 0
        self.burger = h
        self.salads = s
        self.fries = f
        self.soda = so

    def get_cost(self):
        self.cost = ((self.burger * 1.85) + (self.salads * 2.00) + (self.fries * 1.30) + (self.soda * 0.95))
        return self.cost

    def __repr__(self):
        user_cost = "Your order comes to" + str(self.cost)
        return user_cost

h = int(input("Enter number of hamburgers: "))
print("Each hamburger has 9.0g of fat, 33.0g of carbs and 1.0g of fiber")
s = int(input("Enter number of salads: "))
print("Each salad has 1.0g of fat, 11.0g of carbs and 5.0g of fiber")
f = int(input("Enter number of fries: "))
print("Each fries has 11.0g of fat, 36.0g of carbs and 4.0g of fiber")
so = int(input("Enter number of soda: "))
print("Each fries has 0.0g of fat, 38.0g of carbs and 0.0g of fiber")

order = LunchOrder(h, s, f, so)
print(order.get_cost())


##Self Note: learn proper format statement 
