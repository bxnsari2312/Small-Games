##Bansari Shah
##ICS4U-C
##Pg 210 #4;DiceRoll Game
##04/06/2022

import random

class Die:

    def __init__(self):
        self.face = 0

    def roll(self):
        self.face = (random.randint(1,6))
        return self.face

    def __repr__(self):
        return str(self.face)

class Player:

    def __init__(self):
        self.dice1 = (Die())
        self.dice2 = (Die())
        self.points = 1000

    def wager(self, bet, risk):
        print(self.dice1)
        print(self.dice2)
        if ((bet == 0) and (2 <= (int(self.dice1)+int(self.dice2)) <= 6)):
            self.points += (risk*2)
        elif ((bet == 1) and (8 <= int((self.dice1)+int(self.dice2)) <= 12)):
            self.points += (risk*2)
        else:
            self.points -= risk

    def get_points(self):
        return self.points

    def __repr__(self):
        return (str(self.dice1) + str(self.dice2) + str(self.points))

DRPlayer = Player()
while True:
    risks = int(input("risks: "))
    high_low = int(input("high_low: "))
    if risks == -1:
        break
    DRPlayer.wager(high_low, risks)
    print(DRPlayer.get_points())
    points = DRPlayer.get_points()
    print(DRPlayer.get_points())



    
