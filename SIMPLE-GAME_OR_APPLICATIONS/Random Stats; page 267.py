#Bansari Shah
#ICS3U0
#Random stats; page 267
#27 Oct 2020

import random
print("{0:<10s} {1:s}".format("Number", "Occurrences"))

numbers = []
for num in range(500):
    number = random.randint(0, 9)
    numbers.append(number)

zero = numbers.count(0)
one = numbers.count(1)
two = numbers.count(2)
three = numbers.count(3)
four = numbers.count(4)
five = numbers.count(5)
six = numbers.count(6)
seven = numbers.count(7)
eight = numbers.count(8)
nine = numbers.count(9)

index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
occurrences = [zero, one, two, three, four, five, six, seven, eight, nine]

for count in range(len(index)):
    print("{0:<10d} {1:d}".format(index[count], occurrences[count]))


###########################################################################################
import random
print("{0:<10s} {1:s}".format("Number", "Occurrences"))
counts = []
for num in range(10):
    counts.append(0)

for nums in range(500):
    number = random.randint(0, 9)
    if number == 0:
        counts[0] += 1
    elif number == 1:
        counts[1] += 1
    elif number == 3:
        counts[3] += 1
    elif number == 4:
        counts[4] += 1
    elif number == 5:
        counts[5] += 1
    elif number == 6:
        counts[6] += 1
    elif number == 7:
        counts[7] += 1
    elif number == 8:
        counts[8] += 1
    elif number == 9:
        counts[9] += 1

for index in range(len(counts)):
    print("{0:<10d} {1:d}".format(index, counts[index]))
    

















        
    









