##Test Prep; String Problems

##Find common chars in two words
##word1 = input("Enter word 1: ")
##word2 = input("Enter word 2: ")
##
##count = 0
##for chars in word1:
##    for char in range(0, len(word2) - 1, 1):
##        if word2[char] == chars:
##            count += 1
##print(count)
##
###################################################################
##word1 = input("Enter string:")
##word2 = input("Enter String: ")
##
##common = ""
##count = 0
##for chars in word1:
##    if chars in word2:
##        if chars not in common and chars != " ":
##            count += 1
##            common += chars
##print(common)
##print(count)
###################################################################
####Check Palindrome
##            
##word = input("Enter string: ")
##check = (len(word) // 2)
##palindrome = True
##
##for char in range(check):
##    index = (char + 1)*-1
##    index = word[index]
##    if word[char] != index:
##        palindrome = False
##        break
##print(palindrome)
################################################################
####convert alternate characters to capital letters
##word = input("Enter Word: ")
##new = ""
##for chars in range(len(word)):
##    if chars % 2 == 0:
##        new += word[chars]
##    else:
##        new += word[chars].upper()
##print(new)
################################################################
####read a date (dd-mm-yyyy) and print the month name according the month number.
##
##date = input("Enter date: ")
##index = 3
##if date[index] != "0":
##    if date[index + 1] == "0":
##        print("Oct")
##    elif date[index + 1] == "1":
##        print("Nov")
##    else:
##        print("Dec")
##else:
##    if date[index + 1] == "1":
##        print("Jan")
##    elif date[index + 1] == "2":
##        print("Feb")
##    elif date[index + 1] == "3":
##        print("Mar")
##    elif date[index + 1] == "4":
##        print("Apr")
##    elif date[index + 1] == "5":
##        print("May")
##    elif date[index + 1] == "6":
##        print("Jun")
##    elif date[index + 1] == "7":
##        print("Jul")
##    elif date[index + 1] == "8":
##        print("Aug")
##    elif date[index + 1] == "9":
##        print("Sep")
        
####################################################################
##reverse a string without using builtin methods

word = input("Enter a string: ")   ##Enter str
new = ""                           ##For new str

for char in word:                  ##Go through each char in word
    new = char + new   ##New word is going to be keep added next letters as we procecced 
print(new)
    
    
    

        

    


        
            
            
            
        



