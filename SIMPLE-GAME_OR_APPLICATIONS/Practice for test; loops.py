##Slove more loop problems

num1, num2, num3, num4 = input().split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)

for i in range(3):
    print(num1, num2, num3, end = " ")
    num4 += 1
    print(num4)

num2 += 1
num3 = 0
num4 = 0
for j in range(2):
    print(num1, num2, num3, num4)
    num4 += 1
    

################################################################################
##a,b,c=0,0,0. Write a python program to print all permutations using those three variables. Output: 000, 001, 002,.......999.
for i in range(0,10):           
    for j in range(0,10):
        for k in range(0,10):
            print(i, j, k)

   
    

