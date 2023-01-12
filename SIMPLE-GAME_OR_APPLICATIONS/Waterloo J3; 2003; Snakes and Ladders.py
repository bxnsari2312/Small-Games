##Bansari Shah
##ICS3U0
##Waterloo J3; 2004
##2 Nov 2020

step = 1
while True:
    dice = int(input("Enter sum of dice: \n"))
    if dice == 0:
        print("You Quit!")
        break
    step += dice
    if step == 9:
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
    elif step > 100:
        step -= dice
        
    if step != 100:
        print("You are now on the square", step)
    else:
        print("You Win!")
        break

