##Bansari Shah
##ICS4U-C
##2010 S1: Computer Purchase
##05/01/2022

##Formula: value = (2 * R + 3 * S + D )


def value(specs):
    R = int(specs[1])
    S = int(specs[2])
    D = int(specs[3])
    value = (2 * R + 3 * S + D )
    return value 
    
#file = open("S2_2010.text", "r")
##for line in file:
##data.append(line)
##data.pop(0)
data = []
num = int(input())
for i in range(num):
    data.append(input().split())
print(data)

values = [value(data[i]) for i in range(len(data))]
index1 = values.index(max(values))
print(data[index1][0])
values.pop(index1)
index2 = values.index(max(values))
print(data[index2][0])

 
