#Bansari Shah
#ICS3U0
#Question 2; Test Loops and Strings
#23 Oct 2020

##Personal Note:
##Major = 4 years
##Treasurer = 2 years
##Programmer = 3 years
##Dog = 5 years

##Enter input integer for the current year, used \n to print on next line
start = int(input("Enter the current year:\n"))
##Enter input integer for the end year, used \n to print on next line
end = int(input("Enter the future year:\n"))      

##For the start to end of years included
for nums in range(start,(end+1), 1):
    ##divide; is the difference in years from the current year in loop, and ##the starting year[2004-2004 = 0]
    divide = nums - start
    ##If the divide is divisible by 4 move on the next check, that year the ##major changed 
    if (divide % 4) == 0:
        ##If the divide is divisible by 2 and 4, that year the major and ##treasurer changed
        if (divide % 2) == 0:
            ##If the divide is divisible by 2, 3, 4, that year the major and ##treasurer, and programmer changed 
            if (divide % 3) == 0:
                ## If the divide is divisible by 2, 3, 4, 5 that year all changed 
                if (divide % 5) == 0:
                    ##Since all positions changed print out the year; then it ##repeats to check of next year until the last year
                    print("All positions change in year",nums)

