#Bansari Shah
#ICS3U0
#Monogram; Page 155
#17 Oct 2020

first = input("Enter your first name: ")
mid = input("Enter your middle initial: ")
last = input("Enter your last name: ")

mono_first = first[0].lower()
mono_mid = mid[0].lower()
mono_last = last[0].upper()

monogram = mono_first + mono_last + mono_mid
print("Your monogram is:", monogram)
