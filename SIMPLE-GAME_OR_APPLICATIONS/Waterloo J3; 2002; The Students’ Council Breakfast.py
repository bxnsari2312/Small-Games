##Bansari Shah
##ICS3U0
##Waterloo J3; 2002
##2 Nov 2020

pink = int(input("Cost of PINK tickets: \n"))
green = int(input("Cost of GREEN tickets: \n"))
red = int(input("Cost of RED tickets: \n"))
orange = int(input("Cost of ORANGE tickets: \n"))
price_raise = int(input("How much must be raised with ticket sales? \n"))

combinations = []

num_pink = price_raise // pink
num_green = price_raise // green
num_red = price_raise // red
num_orange = price_raise // orange

for p in range(num_pink+1):
    for g in range(num_green+1):
        for r in range(num_red+1):
            for o in range(num_orange+1):
                if (((p*pink)+(g*green)+(r*red)+(o*orange)) == price_raise):
                    combinations.append([p,g,r,o])

for printing in range(len(combinations)):
    print("# of PINK is {0:d}    # of GREEN is {1:d}    # of RED is {2:d}    # of ORANGE is {3:d}".format(combinations[printing][0], \
          combinations[printing][1], combinations[printing][2],combinations[printing][3]))
print("Total combination is", len(combinations), ".")

if len(combinations) == 0:
    print("Minimum number of ticket to print is 0")

else:
    #Get min list
    minimum = 1
    for num in range(len(combinations)):
        for nums in range(len(combinations[num])):
            if combinations[num][nums] < minimum and combinations[num][nums] != 0:
                minimum = combinations[num][nums]
    print("Minimum number of ticket to print is", minimum)
