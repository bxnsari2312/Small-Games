##Bansari Shah
##ICS3U0
##PythagoreanTriple
##13 Nov 2020

import math
from math import sqrt

def perfectSquare(a, b):
    if sqrt(a**2 + b**2).is_integer():
        answer = str(a) + " " + str(b)
    return(answer)

for i in range(1, 101, 1):
    for u in range(1, i+1, 1):
        print(perfectSquare(i, u))
        
        
        
    
    
