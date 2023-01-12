##Bansari Shah
##ICS3U0
##Waterloo J4; 2019
##11 Nov 2020

##get the flips input as str
flips = input()
##Turn the gird into a list
grid = [1,2,3,4]

#For index in the flips; look at each instruction
for index in flips:
    ##if index is V; flips vertical - Each time grid is fliped vertical do..
    if index == "V":
        #save the index 0 in var temp so you can use it for later use
        temp = grid[0]
        #grid at index 0 switches with grid at index 1
        #index 0 now has the value of index at 1
        grid[0] = grid[1]
        #index at 1 now has the original value temp --> index of 0
        grid[1] = temp
        #save temp_2 as value of index of 2
        temp_2  = grid[2]
        #grid at index 2 switches with grid at index 3
        #Save index at 2 to value of index at 3
        grid[2] = grid[3]
        #index of 3 now has the value of temp_2 --> index at 2
        grid[3] = temp_2
    ##if index is H; flips horizontally - Each time grid is flipped horizontally do..
    elif index == "H":
        #save the index 0 in var temp so you can use it for later use
        temp = grid[0]
        #grid at index of 0 switches with grid at index 2
        ##index 0 now has the value of index at 2
        grid[0] = grid[2]
        ##index at 2 now has the original value temp --> index of 0
        grid[2] = temp
        #save temp_2 as value of index of 1
        temp_2  = grid[1]
        #grid at index of 1 switches with grid at index 3
        #Save index at 1 to value of index at 3
        grid[1] = grid[3]
        ##index of 3 now has the value of temp_2 --> index at 1
        grid[3] = temp_2

##Print the resulting first row
print(grid[0], grid[1])
##Print the resulting second row
print(grid[2], grid[3])
