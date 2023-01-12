##Bansari Shah
##ICS4U-C
##2015 S1: Zero That Out
##05/01/2022

k = int(input())
nums = []

for i in range(k):
    num = int(input())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)

total = sum(nums)
print(total)
            

