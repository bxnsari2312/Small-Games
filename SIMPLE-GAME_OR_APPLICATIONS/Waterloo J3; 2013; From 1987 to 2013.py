#Bansari Shah
#ICS3U0
#J3 2013; From 1987 to 2013

##Enter str input year
year = input()
##set diff variable for the int version of year
int_year = int(year)

##Set distinct variable to boolean false
distinct = False

##While distinct is false 
while distinct == False:
    ##Add one to the int year; start comparing from the next year
    int_year += 1
    ##year now has the str value of the new int year
    year = str(int_year)
    ##check all digits in year
    for index in year:
        ##if year has repeated digits
        if str(year).count(index) > 1:
            ##distinct is false
            distinct = False
            ##break for loop, and add one more to current year in the while loop
            break
        ##check if the last digit 
        if year.index(index) == (len(year)-1):
            ##if the last digit is repeated only once
            if str(year).count(index) == 1:
                ##set distinct to True; while loop breaks
                distinct = True
print(year)
                
           
