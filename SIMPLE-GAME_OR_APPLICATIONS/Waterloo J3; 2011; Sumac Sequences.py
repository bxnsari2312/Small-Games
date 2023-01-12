#Bansari Shah
#ICS3U0
#Waterloo J3; 2011
#29 Oct 2020

Num1 = int(input())
Num2 = int(input())

count = 2
while Num1 >= Num2 and Num1 >= 0 and Num2 >=0:
    Num3 = Num1 - Num2
    Num1 = Num2
    Num2 = Num3
    count += 1
print(count)
    
    
