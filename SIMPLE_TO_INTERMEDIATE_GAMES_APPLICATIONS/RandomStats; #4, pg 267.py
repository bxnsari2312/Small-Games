##Bansari Shah
##ICS4U-C
##Random Stats
##02/14/2022

import random
random_num = []
num_repeat = [0,0,0,0,0,0,0,0,0,0]
for element in range(0, 500, 1):
    num = random.randint(0,9)
    num_repeat[num] += 1
for val in range(0, len(num_repeat)+1, 1):
    print("{0:<10d} {1:d}".format(val, num_repeat[val]))
    
    


