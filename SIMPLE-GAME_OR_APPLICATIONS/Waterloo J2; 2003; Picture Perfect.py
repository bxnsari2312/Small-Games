#Bansari Shah
#ICS3U0
#Waterloo J2; 2003
#21 Oct 2020

import math
from math import sqrt
from math import floor

num_list = []
while True:
    num_pic = int(input("Enter number of pictures:  \n"))
    if num_pic ==0:
        break
       
    answer = True
    for factors in range(2, num_pic):
        if  num_pic % factors == 0:
            answer = False

    if answer == True:
        length = 1
        width = num_pic
        
    elif math.isqrt(num_pic) ** 2 == num_pic:
        length = int(sqrt(num_pic))
        width = int(sqrt(num_pic))
        
    else:
        num_list += [1]
        for nums in range(len(num_list)):
            for counter in range(2,num_pic+1, 1):
                if num_pic % counter == 0:
                    num_list += [counter]

        index = len(num_list)// 2
        length = num_list[index]
        width = num_pic // length

    perimeter = 2 * (width + length)
    
    print("Minimum perimeter is", perimeter,"with dimensions", length,"X", width)
                
            
            
        
        
        
        
