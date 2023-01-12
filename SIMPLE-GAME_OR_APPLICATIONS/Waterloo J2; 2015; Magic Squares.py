#Bansari Shah
#ICS3U0
#Waterloo J2; 2015
#18 Oct 2020

row1 = input().split()
row2 = input().split()
row3 = input().split()
row4 = input().split()

total1 = 0
total2 = 0
total3 = 0
total4 = 0

for items in row1:
    items = int(items)
    total1 += items
for items in row2:
    items = int(items)
    total2 += items
for items in row3:
    items = int(items)
    total3 += items
for items in row4:
    items = int(items)
    total4 += items

if(total1 == total2 == total3 == total4):
    for counter in range(4):
        row1[counter] = int(row1[counter]) 
        row2[counter] = int(row2[counter])
        row3[counter] = int(row3[counter])
        row4[counter] = int(row4[counter])
        if (row1[counter] + row2[counter] + row3[counter] + row4[counter] != total1):
            print("not magic")
            break
        else:
            print("magic")
            break
else:
    print("not magic")
            

    
    
    
