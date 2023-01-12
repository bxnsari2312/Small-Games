#Bansari Shah
#ICS3U0
#Problem J1 - Trident; 2003
#21 Oct 2020

length = int(input("Enter tine length: "))
spacing = int(input("Enter tine spacing: "))
handle_len = int(input("Enter handle length: "))

for nums in range(length):
    print("*" + " "*spacing + "*" + " "*spacing + "*" )

print("*"*3 + "*"*spacing*2)

for counts in range(handle_len):
    print(" "*(spacing + 1) + "*" + " "*(spacing + 1))
              
