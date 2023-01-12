#Bansari Shah
#ICS3U0
#Waterloo J2; 2014
#18 Oct 2020

total = int(input())
votes = input()

if total == len(votes):
    count_A = votes.count("A")
    count_B = votes.count("B")
    if count_A > count_B:
        print("A")
    elif count_A < count_B:
        print("B")
    else:
        print("Tie")
