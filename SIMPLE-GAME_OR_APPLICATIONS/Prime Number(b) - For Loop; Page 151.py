#Bansari Shah
#ICS3U0
#Prime Number(b) - For Loop; Page 151
#21 Oct 2020

num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))


for divisibles in range(num1, (num2 +1), 1):
    if divisibles > 1:
        for factor in range(2, divisibles):
            if  divisibles % factor == 0:
                break
        else:
            print(divisibles)


            
            
            
            
