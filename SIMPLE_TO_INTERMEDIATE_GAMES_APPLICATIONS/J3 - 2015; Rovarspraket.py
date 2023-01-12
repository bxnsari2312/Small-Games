##Bansari Shah
##ICS4U-C
##J3 - 2015; Rovarspr¨aket
##02/20/2022

##Take the unecode values of all the vowels;
##vowels = [a, e, i, o, u]
vowels = [97, 101, 105, 111, 117]          
user_word = input()                                             ##Get new input word
new = ""                                                        ##Initialize a new word

##Create a for loop to check each each char 
for char in user_word:                                          
    if (ord(char)) not in vowels:                               ##If the char is not a vowel (comparing the unicode val)
        new += (char)                                           ##1. done - In the new string add the char (letter)
        
        compares = []                                           ##Create a new list to compare the char and vowels 
        ##Create for loop to compare the values of the vowels 
        for compare in vowels:                      
            difference = abs(compare - (ord(char)))             ##get the diff between each vowel and the char comparing(unicode), append to list
            compares.append(difference)
        closest = min(compares)                                 ##Using the min function; find the closet value in the list - smallest diff
        vowels_closest = chr(vowels[compares.index(closest)])   ##find index where there is smallest diff, and use that same index for the vowels, convert to char         
        new += vowels_closest                                   ##2. done - Add the closest vowel to the new encoded 

        unicode_val = ord(char)                                 ##define the unicode_val and add next char 
        unicode_val += 1
        ##If it is in vowel; add one to move on to the next char
        while (unicode_val in vowels):
            unicode_val += 1
        if unicode_val > 122:                                   ##If unicode val reaches beyond z; it stays as z 
            unicode_val = 122
        unicode_val = chr(unicode_val)                          ##3. done - onvert the unicode_val to chr anf add to new 
        new += unicode_val

    ##If it was a vowel it stays the same 
    else:
        new += char
print(new)
        
            
        



