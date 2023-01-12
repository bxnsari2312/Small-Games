#Bansari Shah
#ICS3U0
#J1 2020; Dog Treats


##int imput for num of small size treats 
small_treats = int(input())
##int imput for num of middle size treats 
medium_treats = int(input())
##int imput for num of large treats 
large_treats = int(input())

##happiness level based on formula 
happiness = 1 * small_treats + 2 * medium_treats + 3 * large_treats

##If result of happiness is greater than 10
if (happiness >= 10):
    ##then dog is happy
    print("happy")
else:
    ##Else the dog is sad 
    print("sad")



