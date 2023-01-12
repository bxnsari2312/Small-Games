#Bansari Shah
#ICS3U0
#Waterloo J2; 2019
#18 Oct 2020

num_lines = int(input())               ##Num lines of data 
nums = []
symbols = []

for count in range(num_lines):        
    num, symbol = input().split()
    num = int(num)
    nums.append(num)
    symbols.append(symbol)
    
for count in range(num_lines):
    print(nums[count] * symbols[count])

    
    
    
