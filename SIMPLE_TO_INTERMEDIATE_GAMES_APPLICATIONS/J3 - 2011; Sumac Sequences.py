##Bansari Shah
##ICS4U-C
##J3 - 2011; Sumac Sequences 
##02/20/2022

##Enter the einouts for the first two numbers
##Set up a var for the diff between the first two and the initial count for the len
num1 = int(input())
num2 = int(input())
diff = 0
count = 1          ##Start with the initial count of 1

##Create a while loop for the diff possible 
while diff >= 0:
    diff = num1 - num2          
    num1 = num2
    num2 = diff
    count += 1
print(count)
    
    




