##Bansari Shah
##ICS4U-C
##J3 - 2000; - Slot Machines
##02/20/2022

##Personal Notes
#1 - pays 30 quarters -> 35
#2 - pays 60 quarters -> 100
#3 - pays 9 quarters -> 10

quarters = int(input("How many quarters does Martha have in the jar?\n"))
machine_1 = int(input("How many times has the first machine been played since paying out?\n"))
machine_2 = int(input("How many times has the second machine been played since paying out?\n"))
machine_3 = int(input("How many times has the third machine been played since paying out?\n"))

rounds = 0
while quarters > 0:
    machine_1 += 1
    if machine_1 % 35 == 0:
        quarters += 35
        ##Quarters checked out, so machine resets
        machine_1 = 0
    rounds += 1
    quarters -= 1

    if quarters > 0:
        machine_2 += 1
        if machine_2 % 100 == 0:
            quarters += 60
            machine_2 = 0
        rounds += 1
        quarters -= 1

    if quarters > 0:
        machine_3 += 1
        if machine_3 % 10 == 0:
            quarters += 9
            machine_3 = 0
        rounds += 1
        quarters -= 1

print("Martha plays", rounds, "times before going broke.")
