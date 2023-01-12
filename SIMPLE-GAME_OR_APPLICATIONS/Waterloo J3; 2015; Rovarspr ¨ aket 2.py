#Bansari Shah
#ICS3U0
#Waterloo J3; 2015


vowels = [97, 101, 105, 111, 117]
user_word = input()
new = ""

for char in user_word:
    unicode_val = ord(char)
    if unicode_val not in vowels:
        unicode_val = chr(unicode_val)
        new += unicode_val

        compares = []
        unicode_val = ord(char)
        for compare in vowels:
            difference = abs(compare - unicode_val)
            compares.append(difference)
        closest = min(compares)
        index_compare = compares.index(closest)
        vowels_closest = vowels[index_compare]
        vowels_closest = chr(vowels[index_compare])
        new += vowels_closest

        unicode_val = ord(char)
        unicode_val += 1
        while (unicode_val in vowels):
            unicode_val += 1
        if unicode_val > 122:
            unicode_val = 122
        unicode_val = chr(unicode_val)
        new += unicode_val
        
    else:
        unicode_val = chr(unicode_val)
        new += unicode_val
print(new)
        
            
        

        


        

        
        
            

        
        
            
    
