#Bansari Shah
#ICS3U0
#Prime Numbers(b); Page 150
#10 Oct 2020

num1 = int(input("Enter first possitive integer: "))      ##Get input, first possitive integer 
num2 = int(input("Enter second possitive integer: "))     ##Get input, seconf possitive integer

count = num1                                                  ##Start to check each number from num1

while count < (num2 + 1):       ##Check each integer from num1 to num2(we use (num2 + 1) because we need to set count till num2)                           
    if count > 1:       ##Count has to be greater than 1 cause we are checking the possible factors of count that could make it not prime  
        factor = 2                          ##Assign variable factor the value 2, starts checking the possible values of count from two
        while factor < count:         ##Starts it count from 2 to one less value of count - checks possible factors that make count not prime 
            if count % factor == 0:    ##If count is divisible by factor, then it is not prime 
                break                    ##The loop breaks beacuse that count number is not prime 
            factor += 1                  ##else, you check next possible factor of count 
        if (factor == count):   ##factor has vaue of count because prior step factor is added once more 
            print(count)      #When there are no possible factors from 2 to one less than the num2, the numer is prime; print prime number 
    count += 1                  ##Move on to the next count by adding one 

            
            
            
