##Bansari Shah
##ICS4U-C
##J3 - 2002; - The Students’ Council Breakfast
##02/20/2022

##import itertools
##
##pink = int(input("Cost of PINK tickets: \n"))
##green = int(input("Cost of GREEN tickets: \n"))
##red = int(input("Cost of RED tickets: \n"))
##orange = int(input("Cost of ORANGE tickets: \n"))
##price_raise = int(input("How much must be raised with ticket sales? \n"))
##
##combination_list = []
##tickets_list = [pink, green, red, orange]
##sums2 = []
##
##for indexs in range (len(tickets_list)+1):
##    combination_list += list(itertools.combinations(tickets_list, indexs))
##print(combination_list)
##
##for com in range(len(combination_list)):
##    combination_list[com] = list(combination_list[com])
##    sums = 0
##    for values in range(len(combination_list[com])):
##        sums += int(combination_list[com][values])
##    sums2.append(sums)
##print(sums2)

##################################################################################################################################################################

##Get input for the ticket cost
pink = int(input("Cost of PINK tickets: \n"))
green = int(input("Cost of GREEN tickets: \n"))
red = int(input("Cost of RED tickets: \n"))
orange = int(input("Cost of ORANGE tickets: \n"))
price_raise = int(input("How much must be raised with ticket sales? \n"))

##Create a list for the combinations 
combinations = []

##The total number of tickets present 
num_pink = price_raise // pink
num_green = price_raise // green
num_red = price_raise // red
num_orange = price_raise // orange

##Create a nested list expoloring through all the possible combinations of the list; if the value of all the tickets is equal to the prixe raise; print out combination
for p in range(num_pink+1):
    for g in range(num_green+1):
        for r in range(num_red+1):
            for o in range(num_orange+1):
                if (((p*pink)+(g*green)+(r*red)+(o*orange)) == price_raise):
                    combinations.append([p,g,r,o])
print(combinations)

##length of the combination is the length of possible tickets to print 
for printing in range(len(combinations)):
    print("# of PINK is {0:d}    # of GREEN is {1:d}    # of RED is {2:d}    # of ORANGE is {3:d}".format(combinations[printing][0], \
          combinations[printing][1], combinations[printing][2],combinations[printing][3]))
print("Total combination is", len(combinations), ".")

if len(combinations) == 0:
    print("Minimum number of ticket to print is 0")

##Create a nested loops checking through all the combinations for the tickets to print out
mins = []
else:
    for indexs in range(len(combinations)):
        for j in range(len(combinations[indexs])):
            
        

