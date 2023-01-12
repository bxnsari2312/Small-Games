##Bansari Shah
##ICS4U-C
##2022 S1: Good Fours and Good Fives
##04/25/2022

num = int(input())
count_5 = 0
ans = 0

for i in range(num):
    remainder = (num-count_5*5)
    if remainder > 0:
        count_5 += 1
        if remainder % 4 == 0:
            ans += 1
print(ans)


#########################################################################################################


##num = int(input())
##ans = 0
##
##for i in range(1000000):
##    total = i*5
##    rem = num-total
##    if (rem >= 0 and rem%4 == 0):
##        ans += 1
##
##print(ans)
