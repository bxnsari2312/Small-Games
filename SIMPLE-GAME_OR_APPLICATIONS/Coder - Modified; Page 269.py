#Bansari Shah
#ICS3U0
#Coder; page 269
#30 Oct 2020

string = input("Enter a string: ")
shift = int(input("Enter shift: "))
new = ""
for chars in string:
    unicode_char = ord(chars)
    if (97 <= unicode_char <= 122):
        unicode_char += shift
        if unicode_char > 122:
             unicode_char = unicode_char - 122
             unicode_char = unicode_char + 97
             unicode_char = chr(unicode_char)
             new += unicode_char
        else:
            unicode_char = chr(unicode_char)
            new += unicode_char
    else:
        new += chars
print(new)
        
        
             
             
            
            
        
        
