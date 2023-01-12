##Bansari Shah
##ICS3U0
##Waterloo J4; 2020


word = input()
cycle_shift = input()

possible_shift = []

for index in range(len(cycle_shift)):
    ##This basically rotates the word and gets all possible shift based on the length of the string
    possible_shift.append(cycle_shift[index:]+cycle_shift[:index])
    print(possible_shift)

shift = False


for shifts in possible_shift:
    if shifts in word:
        shifts = True
        break

if shifts == True:
    print("Yes")
else:
    print("No")
    



























        
    
