##Practice for test - Part 2

##Write a python program to read three numbers (a,b,c) and check how many numbers between ‘a’ and ‘b’ are divisible by ‘c’
a = int(input("Enter input a: "))
b = int(input("Enter input b: "))
c = int(input("Enter input c: "))

count = 0
for nums in range(a, b+1, 1):
    if nums % c == 0:
        count += 1
print(count)

##Output =
#1-----99

#2-----98

#3-----97

##. .

#98-----2

#99-----1

num_left = 1
num_right = 99

for nums in range(1, 100):
    print(num_left, "-----", num_right)
    print("")
    num_left += 1
    num_right -= 1

##Convert Number to Binanry
num = int(input("Enter Number: "))  ##Enter a number 
new_num = ""                        ##You want the ew number to be a string 
while num != 0:                     ##If the orginal value is not 0, then this will continue
    new_num += str(num%2)           ##You add the remainder of when you didide the num by 2 to string
    num = num // 2      ##This so far gives the reverse of the value since we work from the last digit
    
for numbers in range(len(new_num)-1,-1, -1): ##len-1 gives the last digit, we need to stop at 0, and steps are -1
    print(new_num[numbers], end = " ")       ##This method would unreverse


    

    
    
    
