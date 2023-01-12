##Bansari Shah
##ICS3U0
##Waterloo J4; 2013
##07 Nov 2020

total_mins = int(input())
num_chores = int(input())
chores = []
count = 0

for i in range (num_chores):
    chore_time = int(input())
    chores.append(chore_time)

chores.sort()

for i in range(len(chores)):
    total_mins -= chores[i]
    if total_mins >= 0:
        count += 1
    else:
        break

print(count)
    


    
