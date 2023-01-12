##Bansari Shah
##ICS4U-C
##J3 - 2009; Good Times
##02/20/2022


##Given information: Conversion factors 
##OT = INPUTTED
##BC = -300
##AB = -200
##MB = -100
##ON = OT
##NS = +100
##NL = +130

##Take initial time 
time = int(input())

##Create a function to convert any time 
def region_time(time, additional):                                  ##function parameters are inputted time and conversion factor 
    new_time = time + additional                                    ##New time is the added time; conversion factor 
    
    if new_time > 2400:                                             ##If the new time > 2400; then its next day; -2400 to get morning time
        new_time -= 2400
    
    elif new_time < 0:                                              ##If new time < than 0; day before day; +2400 to get before time
        new_time += 2400

    if new_time % 100 >= 60:                                        ##If the new_time divivded by 100 has a remainder greater than 60; means that its over 1h
        new_time = ((new_time % 100)-60)+(((new_time//100)*100)+100)##Subract the additional mins by 60; and add 1 additional hour
                                                                    ##To increase the hour increase the number by the hour in the hundrerds place value
    new_time = str(new_time)                                        ##Convert new_time to a str
    if len(new_time) == 1:                                          ##Add 3 zeros at front; it is (12am and single digit min)
        new_time = "000"+new_time
    elif len(new_time) == 2:                                        ##Add 2 zeros at front; it is 12am and double dig mins 
        new_time = "00"+new_time
    elif len(new_time) == 3:
        new_time = "0"+new_time                                     ##Add 1 zero at front; it is before 10am
        
    return (new_time)                                               ##Return the converted time

##Based on the region; print out the converted time and region name 
print(region_time(time, 0), "in Ottawa")
print(region_time(time, -300), "in Victoria")
print(region_time(time, -200), "in Edmonton")
print(region_time(time, -100), "in Winnipeg")
print(region_time(time, 0), "in Toronto")
print(region_time(time, 100), "in Halifax")
print(region_time(time, 130), "in St. John's")



