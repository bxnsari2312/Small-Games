##Bansari Shah
##ICS4U-C
##J3 - 2007; Deal or No Deal Calculator
##02/20/2022

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

##Create list for the money value and the case number (both in order)
##Set the initial number of total money to 0
money_amount = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
case_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

##get the number of cases opened
num_cases = int(input())
##for the number of cases opened; remove the amount of money won 
for data in range(num_cases):
    user_picks = int(input())                                         ##user inputs the cases opened
    money_amount.remove(money_amount[case_numbers.index(user_picks)]) ##remove the money amount in the index that the case_number was opened 

##the banker inputs the money to swtich
banker = int(input())
if (sum(money_amount)/len(money_amount)) > banker:                    ##if the avg is greater than banker; then no deal                                                   
    print("No Deal")
else:                                                                 ##Else; there is a deal
    print("Deal")

