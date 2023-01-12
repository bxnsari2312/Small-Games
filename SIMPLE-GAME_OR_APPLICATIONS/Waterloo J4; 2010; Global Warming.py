##Bansari Shah
##ICS3U0
##Waterloo J4; 2010
##07 Nov 2020

##set count to  0
count = 0
##Create a final answer list 
answer = []

#While loop used to get inputs
while True:
    ##length of cases inputted by user as int 
    number_cases = int(input())
    ##if length of cases is 0; break
    if (number_cases == 0):
        break
    ##else set a new list to differences to store differnces in each case
    differnces = []
    ##Get all input temp cases on one line and split at spaces
    temp = input().split()
    ##For i in range length of temp 
    for i in range(len(temp)):
        ##if i is not the last char from input
        if i != (len(temp)-1):
            ##find differnces of each char and store then in differences
            differnces.append((int(temp[i]) - int(temp[i+1]))*-1)

        ##Find the cycles in list, and use another list to store all lengths cycles
            
        ##Use .sort() to find the smallest cycle and store the answer in the list answer
            
        ##print answer 
            

        
            
