##Bansari Shah
##ICS4U-C
##Pg 210 #6; Gameof21
##04/06/2022

import random


class CardDeal:
    def __init__(self):
        self.card = 0

    def get_card(self):
        self.card = random.randint(1,13)
        return self.card

    def __repr__(self):
        return (str(self.card))

class Game21:

    def __init__(self):
        self.pointsP = 0
        self.pointsC = 0
        self.card = CardDeal()

    def player_plays(self):
        plays = self.card.get_card()
        plays2 = self.card.get_card()
        self.pointsP += (plays + plays2)
    
    def player_extra(self):
        plays3 = self.card.get_card()
        self.pointsP += (plays3)
        
    def computer_plays(self):
        plays_c = self.card.get_card()
        plays_2c = self.card.get_card()
        self.pointsC += (plays_c + plays_2c)
        return self.pointsC

    def show_player(self):
        return self.pointsP

    def show_computer(self):
        return self.pointsC

    def __repr__(self):
        return ("Player points: " + str(self.pointsP) + " Computer Points: " + str(self.pointsC))

print("Choices for players: ")
print("1. Plays with two cards")
print("2. Plays with one card")

game = Game21()
while True:
    
    print(game)
    choice = int(input("choose choice to play crads with: "))
    if choice == 1:
        game.player_plays()
    elif choice == 2:
        game.player_plays()
    print(game)
    if (game.show_player() > 21):
        print("Player loses")
        break
    
    print("Now the computer plays")
    game.computer_plays()
    print(game)
    if (game.show_computer() > 21):
        print("Computer loses")
        break
    


        
        
        
        
        
    
        




























        
