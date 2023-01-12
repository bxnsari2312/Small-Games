##Bansari Shah
##ICS3U0
##Waterloo J4; 2016
##5 Nov 2020

##Rush hour = 7am - 10am
##Rush hour = 3pm - 7pm

leave = input()
leave_hour, leave_min = leave.split(":")
leave = int(leave_hour)*60 + int(leave_min)
arrival = leave

##For two hours
for mins in range(120):
    ##Time is between 7 and 10am
    if (420 <= arrival < 600):
        ##takes double the time to travel
        arrival += 2
    ##Time is between 3 and 7 
    elif (900 <= arrival < 1140):
        ##takes double the time to travel
        arrival += 2
    else:
        ##Takes the normal time
        arrival += 1

    ##If the arrival is at 24h, time restarts to hour 0
    if arrival == 1440:
        arrival = 0

mins = arrival % 60
hours = arrival // 60

if hours < 10:
    hours = "0"+str(hours)
if mins < 10:
    mins = "0"+str(mins)

print(str(hours) + ":" + str(mins))

#################################################################################################################
dep = input()
hour,mins = dep.split(":")

    
    


    
    
    

