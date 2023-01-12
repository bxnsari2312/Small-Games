#Bansari Shah
#ICS3U0
#Prime Number - For Loop; Page 151
#16 Oct 2020

##########################################################################################

num = int(input("Enter number: "))

if num > 1:
    for factor in range(2, num):
        if(num % factor == 0):
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")

###########################################################################################

num = int(input("Enter Number: "))             ##get input integer number 
answer = True                                  ##Get the answer as boolean statement 
Factor = num - 1                            ## Factor can't be the number itself or one 

for count in range(factor, 1, -1):  ##Start at factor(num-1), subtract one each time until factor of 3; stop values end one before
    if num % factor == 0:           ##If number is divisible by the factor value; 
        answer = False              ##Answer condition chnages tp boolean False 
        print("Not Prime")          ##Number is not prime 
        break                       ##Loop breaks 
if answer != False:                 ##if after the loop the value of answer is not False 
    print("Prime")                  ##NUmber is prime 
    
####################################################################################
    
        
    
             
        
    
