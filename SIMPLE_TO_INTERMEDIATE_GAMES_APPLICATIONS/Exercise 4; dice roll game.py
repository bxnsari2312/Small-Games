    ##Bansari Shah
##ICS4U-C
##DiceRollGame 
##03/30/2022


import random

class die:

    def __init__(self, dice1=0, dice2=0):
        self.dice1 = dice1
        self.dice2 = dice2
##        self.total = 0

    def randoms(self, dice1, dice2):
        self.dice1 = random.randint(0,6)
        self.dice2 = random.randint(0,6)

    def __repr__(self):
        dice_values = ("value of dice 1 is " + str(self.dice1) + " and the value of the 2nd die is " + str(self.dice2))
        
##        self.total = (self.dice1 + self.dice2)

class points_game:

    def __init__(self, points, risk, call, dice1, dice2):
        self.points = 1000
        self.risk = risk
        self.call = call

    def total_dice(self, dice1, dice2):
        self.total = 0

    def lose_points(self,risk_points):
        self.points -= (risk_points)

    def gain_points(self, risk_points):
        self.points += (2*risk_points)

    def neutral(self, risk_points):
        self.points -= risk_points


##
##class player:
##
##    def __init__(self, points):


while True:
    user_roll = int(input("How many points do you want to risk? (-1 to quit): "))
    if (user_roll == 1):
        break
    else:
        high_or_low = input("Make a call(0 for low, 1 for high): ")
        total = self.dice1 + self.dice2
        
        
    
    

        
        
        
        
