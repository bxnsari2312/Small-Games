#Bansari Shah
#ICS3U0
#Waterloo J2; 2006
#18 Oct 2020

lower_limit = int(input("Enter lower limit of range:\n")) ##Print 1st input on the next line 
upper_limit = int(input("Enter upper limit of range:\n")) ##Print 2nd input on the next line 

RSA = 0 ##Initial RSA count is 0 

for divisor in range(lower_limit, upper_limit + 1): ##Search for the numbers in between the two inputs 
    count = 0                                       ##resets the count to 0 each time for new num
    for i in range(1, divisor + 1):              ##For numbers from 1 to divisors 
        if divisor % i == 0:                     ##If the remainder is 0 means its divisible 
            count += 1                          ##Add one more count 
    if count == 4:                               ##If count is four then add 1 for RSA
        RSA += 1 
print(RSA)                                  ##print amount of RSA numbers

            
                
