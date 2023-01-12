##Bansari Shah
##ICS3U0
##Waterloo J4; 2007
##06 Nov 2010

pharse1 = input()
phrase2 = input()
word1 = []
word2 = []

for i in range(len(pharse1)):
    if pharse1[i].isalpha() == True:
        word1.append(pharse1[i])

for i in range(len(phrase2)):
    if phrase2[i].isalpha() == True:
        word2.append(phrase2[i])

anagram = True

word1.sort()
word2.sort()

if word1 == word2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
        
        
