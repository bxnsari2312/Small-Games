##Bansari Shah
##ICS3U0
##Waterloo J3; 2005
##2 Nov 2020

streets = ["HOME"]
directions = []

while True:
    direction = input()
    directions.append(direction)
    street = input()
    if street == "SCHOOL":
        break
    streets.append(street)
    
print(directions)
print(streets)

for index in range(len(directions)):
    if directions[index] == "R":
        directions[index] = "LEFT"
    else:
        directions[index] = "RIGHT"

for index in range(len(streets)-1, -1, -1):
    if streets[index] == "HOME":
        print("Turn", directions[index], "into your HOME")
    else:
        print("Turn", directions[index], "onto", streets[index], "street")
        
        
        
