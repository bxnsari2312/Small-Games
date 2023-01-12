##Bansari Shah
##ICS4U-C
##J3 - 2003; - Snakes and Ladders
##02/20/2022

##Start at step 1
step = 1

##if dice = 100; or quite then break the while loop
while True:
    dice = int(input("Enter sum of dice: \n"))         ##Enter the dice amoount
    if dice == 0:
        print("You Quit!") 
        break
    step += dice                                       ##Add steps to dice amount
    if step == 9:                                      ##Ladder at 9 to 34
        step = 34
    elif step == 40:
        step = 64
    elif step == 67:
        step = 86
    elif step == 54:
        step = 19
    elif step == 90:
        step = 48
    elif step == 99:
        step = 77
    elif step > 100:                                ##If step is greater than 100; go back the diff 
        step -= dice
        
    if step != 100:                                 ##If its not 100 print the square val or the person wins 
        print("You are now on the square", step)
    else:
        print("You Win!")


