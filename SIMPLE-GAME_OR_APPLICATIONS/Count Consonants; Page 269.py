#Bansari Shah
#ICS3U0
#Count Consonants; page 269
#27 Oct 2020

string = input("Enter text: ")
Vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

count = 0
for chars in string:
    if chars != " " and chars not in Vowels:
        count += 1
print("The number of consonants in", string, "is", count)
        
