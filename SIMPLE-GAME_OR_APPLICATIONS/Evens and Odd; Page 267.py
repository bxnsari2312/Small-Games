#Bansari Shah
#ICS3U0
#Evens and Odd; page 267
#27 Oct 2020

import random
even = []
odd = []
for counter in range(25):
    number = random.randint(0, 99)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
        
print("ODD:")
print(odd)
print("EVEN:")
print(even)
    
