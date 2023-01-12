##Bansari Shah
##ICS4U0-C
##J3 1996; Pattern Generator
##02/17/2022

import itertools


##Create a inital lists to store total length of code and num of ones
##Get number of total patterns from the user 
len_code = []
num_ones = []
total_pat = int(input())


##From the for loop; append the len of code and num of ones to each list for each patter
for i in range (total_pat):
    x, y = (input("enter letters: ").split())
    len_code.append(int(x))
    num_ones.append(int(y))

##initialize the a list for possible shits; 
pos_shifts = []

##Create a for loop; for each iteration first find the code that needs to be arranged
##Then create a nested loop where the first letter would be fixed and rest would shift fwd by one
for num_pat in range(0, len(len_code), 1):
    ans = ("1"*num_ones[num_pat] + "0"*(len_code[num_pat] - num_ones[num_pat]))

    arr = (itertools.permutations(ans))
    print(arr)

####If the length was one; then there is only one possible shift
##    if (len(ans) == 1):
##        pos_shifts.append(ans)
##
####If it was greater than one (can't be less); fix first char, then shift the str fwd, 
##    else:
##        for perm in (ans[1:]):
##            for j in range(len(ans)):
##                arrangements = perm[:j] + ans[0:1] + perm[j:]
##                print(arrangements)

        
##        ##consider each pattern
##        for j in range(len(ans)):
##            ##consider when the first letter is fixed 
##            for index in range(1, len(ans), 1):
##
##                ##for now; ignore the first char
##                ans2 = ans[1:]
##                arrangements = (ans[j] + ans2[index:] + ans2[:index])
##                print(arrangements)
##
##                ##if the arrangement is not repeated append to possible shifts
##                if (arrangements not in pos_shifts):
##                    pos_shifts.append(arrangements)
##
##        ##Print out each pattern code
####        print("The bit patterns are")
##        print(pos_shifts)

        ##empty the pos_shift to compare for the next value
##        pos_shifts = []
##
##
##
##
##
##
##for perm in (ans[1:]):
##    for j in range(len(ans)):
##        perm[:1] + ans[0:1] + perm[1:]
