##Bansari Shah
##ICS4U-C
##J3 - 2014; Double Dice 
##02/20/2022

##Set up the initial scores 
a_score = 100
d_score = 100

##Create empty list for the die rolls for ana and dav 
a = []
d = []

##Get user input for num of rounds 
rounds = int(input())

##For each round 
for points in range(rounds):
    x, y = input().split()              ##Append the val die to ana and dav's list
    a.append(int(x))
    d.append(int(y))

    if (a[points] > d[points]):         ##if in that round; if ana scored higher; then dav loses ana's point 
        d_score -= a[points]
        
    elif (d[points] > a[points]):       ##if in that round; if dav scored higher; then ana loses dav's point 
        a_score -= d[points]

##Print out the final score
print(a_score)
print(d_score)
    
