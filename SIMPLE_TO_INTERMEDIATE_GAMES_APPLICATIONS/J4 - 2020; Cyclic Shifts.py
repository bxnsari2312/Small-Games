##Bansari Shah
##ICS4U-C
##J4 - 2020; Cyclic Shifts
##02/17/2022

##User inputs a str to examine, and  str to compare 
word = input()
cycle_shift = input()

##Append all types of possible shifts in a list; initialize a list
possible_shift = []

##Create a for loop for each letter of the str 
for index in range(len(cycle_shift)):
    ##This basically rotates the word and gets all possible shift based on the length of the string
    possible_shift.append(cycle_shift[index:]+cycle_shift[:index])
    print(possible_shift)

##Set initial shift to false 
#shift = False

##check all char in all possible arrangements of str
##If the str is in the word; then print true --> code ends 
for shifts in possible_shift:
    if shifts in word:
        shifts = True
        break

if shifts == True:
    print("Yes")
else:
    print("No")
    






