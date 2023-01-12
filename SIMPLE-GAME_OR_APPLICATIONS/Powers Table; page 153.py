#Bansari Shah
#ICS3U0
#Powers Table
#14 Oct 2020

import math
from math import pow

print("{:>9} {:>9} {:>9} {:>9} {:>9}".format("x^1", "x^2", "x^3", "x^4", "x^5"))


i = 1 
while i <= 10:
    print("{0:d} {1:>9.2f} {2:>9.2f} {3:>9.2f} {4:>9.2f} ".format(i, pow(i, 2), pow(i, 3), pow(i, 4), pow(i, 5)))
    i += 1
    
    

