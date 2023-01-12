#Bansari Shah
#ICS3U0
#Digits Display; Page 151
#10 Oct 2020

num = (input("Enter a possitive integer: "))
pos = 0 

while pos < len(num):
    print(num[pos])
    pos += 1

    
#####################################################################


num = int(input("Enter a possitive integer: "))
new = []
while True:
    last = num % 10
    new += [last]
    num = num // 10

    if num < 10:
        new += [num]

        for numbers in new:
            print(new[numbers - 1])
        break 
  
#######################################################################

num = int(input("Enter a possitive integer: ")) ##Get int input 
while True:                                 ##While true used, so it can be any amount of digits 
    last = num % 10                         ##To get the last digit took the reaminder of ten
    print(last)                             ##print last digit
    num = num // 10                         ##Moving onto the next digit I divided it by ten and the number given is the 2nd last digit 

    if num < 10:        ##If number is less rhan 10, if the digit at place of 1 remaining 
        print(num)      ##Print the number 
        break           ##code ends 

#####################################################################################
num = int(input("Pos int: "))
new = ""
while True:
    last = num % 10
    last = str(last)
    new = last + new
    num = num // 10
    if num < 10:
        num = str(num)
        new = num + new
        break
for chars in range(len(new)):
    print(new[chars])




    
