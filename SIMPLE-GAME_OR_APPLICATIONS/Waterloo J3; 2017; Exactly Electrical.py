#Bansari Shah
#ICS3U0
#Waterloo J3; 2017


##Output Y if it is possible to move from the starting coordinate to the destination coordinate using
##exactly t units of electrical charge. Otherwise output N.
import math
from math import sqrt

##get the starting coordinates in from of str then convert them to a list
start = input().split()
##Convert the coordinates to int values
for i in range(2):
    start[i] = int(start[i])
    
##Get the destination coordinates; and turn them into int values 
destination = input().split()
for i in range(2):
    destination[i] = int(destination[i])

##Get the unit charge value as int inputs 
units_charge = int(input())

##Distance formula to find min distance
distance = sqrt(((start[0]-destination[0])**2) + ((start[1]-destination[1])**2))

##If the distance is greater than unit charge means that it is not enough to reach destination
if distance > units_charge:
    print("N")
##If distance and unit charge are both(even/ odd); it is possible 
elif distance % 2 == units_charge % 2:
    print("Y")
##else the other option is that its not Y
else:
    print("N")
