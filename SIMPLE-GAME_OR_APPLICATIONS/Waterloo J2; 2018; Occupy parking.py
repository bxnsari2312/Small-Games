#Bansari Shah
#ICS3U0
#J2 2018; Occupy parking


##int imput for total num of spaces 
spaces =  int(input())
##list for yesterday's data
yes_data = []
##list for today's data
today_data = []
##inital value of spaces occupied 
occupied = 0

##str input for yesterday's parking arrangement 
yesterday = input()
##str input for today's parking arrangement 
today = input()

##check all items in range of number of spaces 
for items in range(spaces):
    ##append yesterday's data to yes_data
    yes_data.append(yesterday[items])
    ##append todays's data to today_data
    today_data.append(today[items])

for counter in range(spaces):
    ##if the same index in both the list is "C"
    if (yes_data[counter] == today_data[counter] == "C"):
        ##Add one to occupied
        occupied += 1
print(occupied)
        
