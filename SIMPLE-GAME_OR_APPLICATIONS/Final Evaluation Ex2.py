##Bansari Shah
##ICS3U0
##Final Evaluation Ex2
##09 Nov 2020

##Get input as str for hour
Hour = (input("Hour  :"))
##Get input as str for mins
Min = (input("Minute:"))
##Get input as str for the current day
Day = (input("Day   :"))

##Concatenate hour and mins and turn them to int to get the 24h Ottawa time
time = int(Hour+Min)

##Function for converting the ottawa time to regional time based on the time differences in the regions 
def regions_time(ottawa_time, difference):
    ##The new_time is the ottawa time plus the time difference 
    new_time = (time + difference)
    ##Set orginal day value to the "Same day"
    day = "Same Day"
    
    ##When the new_time is greater than or equal 2400
    if (new_time >= 2400):
        ##new_time is the subtracted an addtional day(2400); gets the raw time of the new region
        new_time -= 2400
        #it is the next day; since its passed 24hs
        day = "Next Day"

    ##When the new_time is less than 0hs 
    elif (new_time < 0):
        ##new_time is the added the an day; get the raw time of the new region
        new_time += 2400
        ##it was yesterday; since its less than present day(00:00)
        day = "Previous Day"

    ##If the new_time divivded by 100 has a remainder greater than 60; means that its over 1h
    if ((new_time % 100) >= 60):
        ##Subract the additional mins by 60; and add 1 additional hour
        ##To increase the hour increase the number by the hour in the hundrerds place value 
        new_time = ((new_time % 100)-60)+(((new_time//100)*100)+100)

    ##Turn new_time into a string 
    new_time = str(new_time)

    ##If new_time only has one digit; only possibility is that the hour is 00 and the mins are less than 10
    if len(new_time) == 1:
        ##Add 3 zeros at front; it is (12am and single digit min)
        new_time = "000"+new_time
    ##if new_time only has two digits; only possibility is that the hour is 00 
    elif len(new_time) == 2:
        ##Add 2 zeros at front; it is (12am and mins)
        new_time = "00"+new_time
    ##if new_time only has three digits; only possibility is that hour is one digit
    elif len(new_time) == 3:
        ##Add 1 zero at front; less than 10am 
        new_time = "0"+new_time
        
    ##final answer is the day value, and the new_time value
    answer = (day+ " " +new_time)
    ##return the ouput of answer
    return answer

##Used the function regions_time with the parameters of Ottawa time and the time difference to get the final answer:

##Ottawa there is no time difference 
print(regions_time(time, 0), "in Ottawa")
##Victoria is 3hs behind 
print(regions_time(time, -300), "in Victoria")
##Edmonton is 2hs behind 
print(regions_time(time, -200), "in Edmonton")
##Winniped is 1h behind 
print(regions_time(time, -100), "in Winnipeg")
##Toronto there is no time differnce 
print(regions_time(time, 0), "in Toronto")
##Halifax is 1h ahead 
print(regions_time(time, 100), "in Halifax")
##St. John's is 1h30mins ahead 
print(regions_time(time, 130), "in St. John's")
##India time 
print(regions_time(time, 1030), "in India")

    

        
        
        

