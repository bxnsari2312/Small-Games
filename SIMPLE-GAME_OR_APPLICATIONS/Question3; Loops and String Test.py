#Bansari Shah
#ICS3U0
#Question 3; Test Loops and Strings
#23 Oct 2020

##Enter input integer to get the num
num = int(input("Give the number: "))
##Enter input integer to get the number of shifts 
shift = int(input("Give the shift value: "))

##Initalize total to num, so that you just have to add product of nums in ##the next steps
total = num
##Initalize the product to num so that is the base, and you are ##multiplying by 10 the remainder times
product = num

##repeat the multiplication of 10 process given the number of shift
for count in range(shift):
    ##The product is the number multiplied by 10
    product *= 10
    ##The total is the total plus the product 
    total += product
##After loop ends print total
print("The shifty sum is:",total)

