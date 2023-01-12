#Bansari Shah
#ICS3U0
#GCD; Page 153
#10 Oct 2020


##Eclids Algorithm; Greatest Common Divisor
##Explained the math in the notebook 


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

while num2!= 0:
    temp1 = num1
    num1 = num2
    num2 = temp1 % num2
print(num1)

    
