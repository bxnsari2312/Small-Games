#Bansari Shah
#ICS3U0
#Waterloo Problem1; 2000
#22 Oct 2020

##Perfect Numbers = sum of its possitive divisors exculding itself

##for num in range(1000, 10000):
##    total = 0
##    for factors in range(1, num):
##        if num % factors == 0:
##            total += factors
##    if total == num:
##        print(num)
            
    
## integers between 100 and 999 inclusive which are equal to the sum of the cubes of their digits


for num in range(100, 1000):
    while True:
        total = 0
        num1 = num
        last = num % 10
        num = num // 10
        total += (last ** 2)
        if num < 10:
            total += num ** 2
        if num1 == total:
            print(num1)
            break
        else:
            break
