##Bansari Shah
##ICS3U0
##Waterloo J4; 2012


##S = 3P+k

shift_k = int(input())
word = input()
new = ""

for letter in range (len(word)):
    
    if (65 <= ord(word[letter]) <= 90):
        S = -1*((3*(letter+1))+shift_k)
        new_shift_value = ord(word[letter])+S
        
        if (65 <= new_shift_value <= 90):
            new += (chr(new_shift_value))
            
        elif (new_shift_value > 90):
            new_shift_value = (new_shift_value-90)+64
            new += (chr(new_shift_value))
            
        elif (new_shift_value < 65):
            new_shift_value = 91 - (65 - new_shift_value)
            new += (chr(new_shift_value))
    else:
        new += (chr(letter))
        
print(new)
            
            
            
            
            
            
        
        
