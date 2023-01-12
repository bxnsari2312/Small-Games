#Bansari Shah
#ICS3U0
#Waterloo J3; 2009
#29 Oct 2020

##Personal Notes:
#1 -> $100
#2 -> $500
#3 -> $1,000
#4 -> $5,000
#5 -> $10,000
#6 -> $25,000
#7 -> $50,000
#8 -> $100,000
#9 -> $500,000
#10 -> $1,000,000

money_amount = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
Case_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

num_cases = int(input())
for data in range(num_cases):
    user_picks = int(input())
    money_amount.remove(Case_numbers)

banker = int(input())
for money in money_amount:
    total += money
if total/(len(money_amount)) > banker:
    print("No Deal")
else:
    print("Deal")

    
    
    
        
