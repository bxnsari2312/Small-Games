#Bansari Shah
#ICS3U0
#Compound Interest; Page 150
#10 Oct 2020

## Finding time it takes to get the amount(compound interest)

## Compound interest is when an amount is you have an amount and you calcuate the rate for first year, then you move on to new amount and use that
## as the principle to calculate the rate for the next year 

Principle = int(input("Enter Principle Amount: "))
Final = int(input("Enter Final Amount: "))
Rate = float(input("Enter Annual Compound Rate: "))
Rate = round((Rate/100), 3)
years = 0
Amount = Principle

while Amount < Final:                      ##Calculate the amount until you get near the final amount 
    Principle = Amount * Rate              
    Amount += Principle
    years += 1
print(years)

    
    
    
