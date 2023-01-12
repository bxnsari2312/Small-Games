##Bansari Shah
##ICS4U-C
##J3 - 2017; Exactly Electrical
##02/20/2022

##Output Y if it is possible to move from the starting coordinate to the destination coordinate using
##exactly t units of electrical charge. Otherwise output N.
import math
from math import sqrt

##get the starting coordinates in from of str and then convert them into int in a list using the map function
start = input().split()
start = list(map(int, start))

##get the end coordinates in from of str, then convert them into int in a list using the map function
end = input().split()
end = list(map(int, end))

##Get the unit charge value as int inputs 
units_charge = int(input())

##Distance formula to find min distance: d = sprt((x2-x1)^2 + (y2-y1)^2))
distance = sqrt(((start[0]-end[0])**2) + ((start[1]-end[1])**2))

##If the distance is greater than unit charge means that it is not enough to reach destination
if distance > units_charge:
    print("N")
##If distance and unit charge are both(even/ odd); it is possible 
elif distance % 2 == units_charge % 2:
    print("Y")
##else the other option is that its not Y
else:
    print("N")
