##Bansari Shah
##ICS4U-C
##2016 S1: Ragaman
##05/01/2022

line1 = input()
line2 = input()
char_index = [0 for i in range(26)]
count_a = 0

for char in line1:
    index = abs(ord(char) - 65)
    char_index[index] += 1
for char in line2:
    if char == "*":
        count_a += 1
    else:
        index = abs(ord(char) - 65)
        char_index[index] -= 1
        
for i in char_index:
    if i > 0:
        count_a -= 1
if a_count == 0:
    print(a_count)
else:
    print("N")
        
        
    
        
        
