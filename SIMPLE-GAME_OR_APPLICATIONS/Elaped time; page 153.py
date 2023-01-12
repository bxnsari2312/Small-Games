#Bansari Shah
#ICS3U0
#Elasped Time Calculator; Page 153
#17 Oct 2020

hour = int(input("Enter the starting hour: "))                         ##Input int for the hour
day_or_night = (input("Enter am or pm: "))                         ##input string for am or pm
time_skip = int(input("Enter number of elasped hours: "))  ##input int for hours skiped 

day_night_ans = "am"                               ##Initial time set to am

if day_or_night == "pm":                           ##Convert to 24h time 
    if (1<= hour <= 11):                              ##if hour is range from 1pm - 11pm
        hour += 12                                        ##Hour += 12 to get miltarty time 
elif (day_or_night == "am") and (hour == 12):   ##If the time is 12am then military time is 24hs
    hour += 12                                                      ##12:am is being converted to 24:00h

total_time = hour + time_skip                           ##Total time skip is hours + time elapsed 

if total_time >= 24:                              ##If total time is greater than 24s(new day)
    total_time %= 24                            ##If many days passed like skip to 48hs then still the remiander works to tell the time 
    if total_time == 0:                           ##If the remiander is 0, then it means that time is 12pm, in different day 
        total_time = 12
if total_time > 12:                              ##Then check that if total time is greater than 12, like for example the remainder is 17
    total_time -= 12                             ##Subtract 12 from it to get the orginal time; so it would be 5pm
    day_night_ans = "pm"                    ##add pm
elif total_time == 12:
    day_night_ans = "pm"


print("The time is:",total_time, day_night_ans)   ##Print final amount




        
    
        
