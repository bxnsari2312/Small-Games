#Bansari Shah
#ICS3U0
#Prime Number - funtion; Page 175
#06 Nov 2020

def isPrime(num):
    prime = True
    
    factor = num - 1
    
    while factor > 1:
        if num % factor == 0:
            prime = False
            break
        
        else:
            factor -= 1
            
    if factor == 1:
        prime = True

    return prime

number = int(input("Enter Number: "))
print(isPrime(number))
    
    
    
