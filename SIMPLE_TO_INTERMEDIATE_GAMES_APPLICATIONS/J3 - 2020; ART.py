##Bansari Shah
##ICS4U-C
##J3 - 2020; ART
##02/17/2022

##Get num of drops
num_drops = int(input())
##Create list for the x and y coordinates 
x_values = []
y_values = []

##Append the given data into the lists for x and y 
for data in range(num_drops):
    data = input()
    x, y = data.split()
    x_values.append(int(x))
    y_values.append(int(y))

##Using the max ans min functions; find the max and min values for x and y
min_y = min(y_values)
min_x = min(x_values)
max_y = max(y_values)
max_x = max(x_values)


##Based on the given diagram; the val of the points are with diff with one(because only integers) with the painting
new_min_x = min_x - 1 ##So it shifts more to the left
new_min_y = min_y - 1 ##So it shifts more down

new_max_x = max_x + 1 ##So it shifts more up
new_max_y = max_y + 1 ##So it shifts more right 

##Based on shifts applied; print out the final diagram
print(new_min_x, new_min_y)
print(new_max_x, new_max_y)
