##Bansari Shah
##ICS4U-C
##J3 - 2005; Returning Home
##02/20/2022

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

##reverse
for index in range(len(streets)-1, -1, -1):
    if index == 0:
        print("Turn", directions[index], "into your HOME")
    else:
        print("Turn", directions[index], "onto", streets[index], "street")



