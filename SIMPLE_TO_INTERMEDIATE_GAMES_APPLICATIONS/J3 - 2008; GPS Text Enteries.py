##Bansari Shah
##ICS4U-C
##J3 - 2008; GPS Text Entry
##02/20/2022

##input a word 
word = input()
##The full word would be "A"+word+"e"; initailly always starts with "A" and always ends at "e"(enter)
full_word = "A"+word+"e"
##Create two lists for the x and y components 
key_board_x = ["ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZ -.e"]
key_board_y = ["AGMSY", "BHNTZ", "CIOU ", "DJPV-", "EKQW.", "FLRXe"]

##Set the initial steps, x, and y, vals to zero and create a list for the coordinates
steps = 0
x = 0
y = 0
coordinates = []                                          

##create a for loop for each char that needs to be considered;
##Objective of loop; convert each char into coordinates points; in terms of (x,y)
for counter in range(len(full_word)):                                
    char = full_word[counter]                                   ##Create a loop to consider each char
    for index in range(len(key_board_x)):                       ##Create a nested loop to consider x steps
        if char in key_board_x[index]:                          ##check if char is in which row(x-dir)
            ##Added one extra for the A
            x = index + 1
    for index in range(len(key_board_y)):                       ##loop to consider y-dir
        if char in key_board_y[index]:                          ##If char is in y-str; then add the y-value  
            y = index + 1
    coordinates.append((x,y))                                   ##in the coordinates list append the x and y values 
                                                                
print(coordinates)
##Consider the whole coordinates list;
for index in range(len(coordinates)-1):                             ##consider; list index; then index inside the list       
    steps += abs(coordinates[index+1][0] - coordinates[index][0])   ##Find the x steps; by sub the next val to current val
    steps += abs(coordinates[index+1][1] - coordinates[index][1])   ##Find the y steps; by sub the next val to current val 
print(steps)
