#Bansari Shah
#ICS3U0
#Waterloo J3; 2015
#28 Oct 2020

string = input()
near_vowel = "aaeeeiiiiooooouuuuuuu"
consonant = "bcdfghjklmnpqrstvwxyz"
next_consonant = "cdfghjklmnpqrstvwxyzz"
new = ""

for index in range(len(string)):
    if string[index] in consonant:
        new += string[index] + near_vowel[consonant.index(string[index])] + next_consonant[consonant.index(string[index])]
    else:
        new += string[index]
print(new)
        
