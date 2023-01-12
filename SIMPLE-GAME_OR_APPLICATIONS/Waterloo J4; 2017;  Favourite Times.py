##Bansari Shah
##ICS3U0
##Waterloo J4; 2017
##5 Nov 2020

hour = 12
mins = 00
count = 0

added = int(input())

for adding in range(added):
    mins += 1
    if mins > 60:
        hour += 1
        mins -= 60
        if hour > 12:
            hour = hour % 12
    if mins < 10:
        new_time = str(hour) + "0" + str(mins)
    else:
        new_time = str(hour) + str(mins)
    if len(new_time) == 4:
        if (int(new_time[3]) - int(new_time[2])) == (int(new_time[2]) - int(new_time[1])) == (int(new_time[1]) - int(new_time[0])):
            count += 1
    else:
        if (int(new_time[2]) - int(new_time[1])) == (int(new_time[1]) - int(new_time[0])):
            count += 1
print(count)
            
        


    
    




    



