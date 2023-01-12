##Bansari Shah
##ICS4U0-C
##J4 2015; Wait Time

num_lines = int(input())
type_ent = []
person = []
wait = [0]*num_lines
send = [0]*num_lines
returns = [0]*num_lines


time = 0

for i in range(num_lines):
    x, y = input().split()
    type_ent.append(x)
    person.append(y)

for j in range(num_lines):
    if (type_ent == "R"):
        returns[j] = -1
        send[j] = time

    elif (type_ent == "S"):
        send[j] += time - send[j]
        returns = 1

    ##subtract for the wait before/ after the start/ end 
    else:
        time += j-2
        
    time += 1

for l in range(num_lines):
    print(l, wait[l]) 
        
        
        
        
    
    
    
