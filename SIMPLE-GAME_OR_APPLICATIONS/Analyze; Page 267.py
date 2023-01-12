#Bansari Shah
#ICS3U0
#Analyze; page 267
#27 Oct 2020

##Python counter returns count of each element in list; and .most_commom tells most repeated
import collections
from collections import Counter

all_num = []
while True:
    number = int(input("Enter num 1-50, enter -1 to quit: "))
    if number == -1:
        break
    else:
        all_num.append(number)

average = ((sum(all_num))/(len(all_num)))
print("Average: ",average)

maximum = max(all_num)
print("Max: ", maximum)

Range = maximum - min(all_num)
print("Range: ", Range)

repeated_count = Counter(all_num)
##Need the index (1)[0][0]; says the first most repeated, and only returns the number not how many times repeated
##(1) = tells the most repeated pair in list
##[0] = gets rid of the extra list
##[0] == only returns median not times it is repeated
median = repeated_count.most_common(1)[0][0]
print("Median: ", median)

##To make an histogram/ bar garph
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0 
count8 = 0
count9 = 0
count10 = 0
for nums in all_num:
    if (1<= nums <= 5):
        count1 += 1
    elif(6<= nums <= 10):
        count2 += 1
    elif(11<= nums <= 15):
        count3 += 1
    elif(16<= nums <= 20):
        count4 += 1
    elif(21<= nums <= 25):
        count5 += 1
    elif(26<= nums <= 30):
        count6 += 1
    elif(31<= nums <= 35):
        count7 += 1
    elif(36<= nums <= 40):
        count8 += 1
    elif(41<= nums <= 45):
        count9 += 1
    elif(45<= nums <= 50):
        count10 += 1
ranges = ["1 - 5:","6 - 10:","11 - 15:","16 - 20:","21 - 25:", "26 - 30:", "31 - 35:", "36 - 40:", "41 - 45:", "46 - 50:"]
counting = [count1, count2, count3, count4, count5, count6, count7, count8, count9, count10]

for index in range(len(ranges)):
    print("{0:>10s} {1:s}".format(ranges[index], ("*"*(counting[index]))))

















        
        
