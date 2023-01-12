##Bansari Shah
##ICS4U-C
##2021 S1: Crazy Fencing
##05/01/2022

n = int(input())
height = input().split()
height = [int(x) for x in height]
width = input().split()
width = [int(x) for x in width]
total_area = 0

##Ar(trapezoid) = ((a+b)h)/2
#total_area += ((((height[i] + height[i+1])*width[i])/2) for i in range(n))
for i in range(n):
    total_area += (height[i]+height[i+1])*width[i] /2
print(total_area)





