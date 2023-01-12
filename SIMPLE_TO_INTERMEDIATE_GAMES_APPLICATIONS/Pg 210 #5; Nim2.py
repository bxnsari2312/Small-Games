##Bansari Shah
##ICS4U-C
##Pg 210 #5; Nim2 
##04/04/2022

##Code description:
##The Nim game is a game where a player and a computer ulternate to take out points, the last one to take out the point loses 
##
##import random
##
##class Nim2:
##
##    def __init__(self):
##        self.points = 0
##
##    def start_stones(self):
##        self.points = random.randint(15,30)
##        return self.points
##    
##    def set_points(self, initial_points):
##        self.points = initial_points
##        return self.points
##
##    def player_plays(self, take_point):
##        self.points -= take_point
##        return self.points
##
##    def computer_takes(self):
##        computer_takes = random.randint(1,3)
##        return computer_takes
##
##    def computer_plays(self):
##        self.points -= game.computer_takes()
##        return self.points
##
##    def display_points(self):
##        return self.points
##
##    def __repr__(self):
##        data = f"Current Points: {self.points}"
##        return data
##
##game = Nim2()
##initial_points = game.start_stones()
##points = game.set_points(initial_points)
##print(points)
##
##while (points > 0):
##    take_point = int(input("Enter the number stones to take out: "))
##    while (game.points < take_point):
##        take_point = input("Error, illegal number of points played, enter new amount: ")
##    points = game.player_plays(take_point)
##    print(Nim2())
##        
##    if game.points == 0:
##        print("You lose")
##        break
##
##    else:
##        take_point = game.computer_takes()
##        while (game.points < take_point):
##            take_point = game.computer_points()
##        points = game.computer_plays()
##        print(Nim2())
##        

###########################################################################################################
import random
class Nim2:

    def __init__(self, turn = 0):
        self.points = 0

    def start_stones(self):
        self.points = random.randint(15,30)
        return self.points

    def set_points(self, initial_points):
        self.points = initial_points
        return self.points

    def player_plays(self, take_point):
        self.points -= take_point
        return self.points


    def computer_plays(self,number):
        self.points -= number
        return self.points

    def display_points(self):
        return self.points

    def __repr__(self):
        data = (str(self.points) )
        return data

game = Nim2()
initial_points = game.start_stones()
points = game.set_points(initial_points)
print(points)

while (points > 0):
    take_point = int(input("Enter the number stones to take out: "))
    while (game.points < take_point):
        take_point = int(input("Error, illegal number of points played, enter new amount: "))
    game.player_plays(take_point)
    if game.points == 0:
        print("The player beats the computer.")
    print(game)

    if game.points == 0:
        print("The computer beats the player.")
        break

    take_point = random.randint(1,3)
    while (game.points < take_point):
        take_point = random.randint(1,3)
    game.computer_plays(take_point)
    print("The computer takes:",take_point)
    print(game)


            
            
            
        

        
        
        
        
    

    
        
        

