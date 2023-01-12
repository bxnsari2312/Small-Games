#Bansari Shah
#ICS3U0
#Waterloo J2; 2004
#21 Oct 2020

##Major = 4 years
##Treasurer = 2 years
##Programmer = 3 years
##Dog = 5 years

start = int(input("Enter the current year:\n"))
end = int(input("Enter the future year:\n"))

for nums in range(start,(end+1), 1):
    divide = nums - start
    if (divide % 4) == 0:
        if (divide % 2) == 0:
            if (divide % 3) == 0:
                if (divide % 5) == 0:
                    print(nums)
    
        
        
        
        
        




