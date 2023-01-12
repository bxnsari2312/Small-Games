#Bansari Shah
#ICS3U0
#Prime Number - funtion; Page 175
#06 Nov 2020

print("Enter your total coins: ")
print("")

quarters = int(input("Quarters: "))
Dimes = int(input("Dimes: "))
Nickels = int(input("Nickels: "))
Pennies = int(input("Pennies: "))

def DollarAmount(quarters, Dimes, Nickels, Pennies):
    total = ( quarters*0.25 + Dimes*0.1 + Nickels*0.05 + Pennies*0.01 )
    return str(total)

print("Total: $"+DollarAmount(quarters, Dimes, Nickels, Pennies))
