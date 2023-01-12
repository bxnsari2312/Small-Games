#Bansari Shah
#ICS3U0
#Palindrome; page 267
#27 Oct 2020

string = input("Enter Text: ")
mid = (len(string) // 2)

Palindrome = True
for index in range(mid):
    if string[index] != string[- (index + 1)]:     
        Palindrome = False
        break
if Palindrome == True:
    print(True)
else:
    print(False)

############################################
##string = input().split()
##string.lower()
##print(string)
##word = []
##for char in string:
##    for i in range(len(char)):
##        word.append(char[i])
##Palindrome = True
##for index in range((len(word)//2)):
##    if word[index] != word[- (index + 1)]:     
##        Palindrome = False
##        break
##if Palindrome == True:
##    print(True)
##else:
##    print(False)
##
##
















    
