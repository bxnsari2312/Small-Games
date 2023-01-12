##Bansari Shah
##ICS4U-C
##Pg 210 #7; Bowling
##04/06/2022

import random

class random_knock:

    def __init__(self):
        self.num_k = 0

    def num_knocked(self):
        self.num_k = random.randint(0,10)
        return self.num_k

    def __repr__(self):
        return ("Pins knocked: ",self.num_k)

class score:

    def __init__(self):
        self.pins_k = random_knock()
        self.final_points = 0
        self.pins = 10
        self.points = 0
        self.total_frame_points = 0
        self.frames_tries = 1

    def roll(self):
        while (self.frames_tries <= 2):
            if (self.frames_tries == 1 and self.pins > 0):
                knocked = self.pins_k.num_knocked
                if knocked == 10:
                    self.total_frame_points += 20
                    self.pins -= knocked
                self.total_frame_points += knocked
                self.pins -= knocked
                
            elif (self.frames_tries == 2 and self.pins > 0):
                knocked = self.pins_k.num_knocked
                self.pins -= knocked
                if self.pins == 0:
                    self.total_frame_points += 15 
                self.total_frame_points += knocked
                
        self.points += self.total_frame_points
        self.frames_tries += 1
        self.final_points += self.points
        return (self.final_points)

    def get_final(self):
        return (self.final_points)

player = score()
player2 = score()
frames = 1
while (frames < 10):
    player.roll()
    player2.roll()
    frames += 1
print("Player1 final total: ", player.get_final)
print("Player1 final total2: ", player2.get_final)


                

























                  
