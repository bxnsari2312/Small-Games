#Bansari Shah
#ICS3U0
#Waterloo J2; 2020
#18 Oct 2020

Target = int(input())
Initial = int(input())
Rate = int(input())
day = 0

total = Initial

while total <= Target:
    Initial *= Rate
    total += Initial
    day += 1
print(day)
    
    
    
    
    
