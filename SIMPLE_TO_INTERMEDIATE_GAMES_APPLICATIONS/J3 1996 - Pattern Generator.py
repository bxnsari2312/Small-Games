##Bansari Shah
##ICS4U0-C
##J3 1996; Pattern Generator
##02/16/2022

##Import math to use factorial
import math
import itertools 

##Create empty list for the len of code and num of 1's 
len_code = []
num_ones = []

# abc
# bc
# cb
# 

def perms(string):
    if len(string) == 1:
        return [string]

    for i in range(len(string)):
        string = string[1::] + string[0]
        swaps.append(string)

    x = perms(string[1::])
    new = []
    for elm in swaps:
        for 
    


    return swaps

print(perms("abcd"))
    
    
    


####Enter the total number of pattern types 
##pattern_types = int(input())
##
####For each inputted pattern append the values to two list
##for num in range (0, pattern_types, 1):
##    x, y = (input("Enter two values: ").split())
##    len_code.append(int(x))
##    num_ones.append(int(y))
##
##
##for bit_pat in range(0, )
##    
##    
##
##
####total_pos = int(((math.factorial(len_code[bit_pat])) / (math.factorial(num_ones[bit_pat]) *  math.factorial(len_code[bit_pat]-num_ones[bit_pat]))))
##
##   
##        
##
##
##
##
##
##
##
##
####Find the total number of possible arrangements: (length)! / (num_ones! * len_code!)
##
