##Python if else, for loop, and range()
##1 
##1 2 
##1 2 3 
##1 2 3 4 
##1 2 3 4 5

##Look at numbre of rows; method of pattern
rows = int(input("Enter rows: "))

##Need to for loops, one for rows and other for colums
for i in range(1, rows+1, 1):
    for colums in range(1, i+1, 1):
        print(colums, end = " ") ##After printing the first num, the secound num is imediatly an string
    print("") ##need this to indicate that we are printing on a new line

##Print Output similar to this
##5 4 3 2 1 
##4 3 2 1 
##3 2 1 
##2 1 
##1
rows = int(input("Enter rows: "))    ##Get num of rows
for i in range(rows+1, 0, -1):       ##Starts at max rows and slowy decreases 
    for j in range(i-1, 0, -1):      ##for colums, it dreceases by 1 each time 
        print(j, end = " ")          ##Print colum data on same line 
    print("")                        ##Difreinciate the colum data

##Display fibinocci sequence
terms = int(input("Enter num of terms: "))
num1 = 0
num2 = 1

for nums in range(1, terms+1, 1):
    print(num1, end = " ")
    temp = num1 + num2
    num1 = num2
    num2 = temp

##Find Factorial of any number
num = int(input("Enter number: "))
product = 1
for numbers in range(1, num+1, 1):
    product *= numbers
print(product)

##Reverse a integer number
num = int(input("Enter input: "))
for numbers in range(num):
    last = num%10
    print(last, end = "")
    num = num // 10
    if num < 10:
        print(num)
        break
##Find cubes of integers
num = int(input("Enter number: "))
for num in range(1, num+1, 1):
    print("Current Number is :",num, "and the cube is", num**3)

##Find the sum of the series 2 + 22 + 222 + 2222 + .. n terms
num_terms = int(input("Enter num of terms: "))
start = 2
total = 0
for nums in range(num_terms):
    total += start
    start = (start * 10)+2
print(total)

##Print follwoing pattern;
##* 
##* * 
##* * * 
##* * * * 
##* * * * * 
##* * * * 
##* * * 
##* * 
##*

rows = int(input("Enter num of rows: "))
for i in range(1, rows):
    for colums in range(i):
        print("*", end = " ")
    print("")
for i in range(rows, 0, -1):
    for colums in range(i):
        print("*", end = " ")
    print("")
    








    

    
