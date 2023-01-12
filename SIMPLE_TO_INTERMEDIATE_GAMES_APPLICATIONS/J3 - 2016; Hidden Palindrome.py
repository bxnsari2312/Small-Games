##Bansari Shah
##ICS4U-C
##J3 - 2016; Hidden Palindrome
##02/20/2022

##get user input str
string = input()                        ##Get user input
largest_length = 0                      ##Set initial largest len to 0
                            
##Need to use len(string)+1 for slicing
for counter in range(len(string)+1):                              ##loop through all the char of str 
    for index in range(counter, len(string)+1):                   ##Nested loop; index from counter to remaining of letters
        encode_string = string[counter:index]                     ##Consider the str from the counter to the index(not inc)
        ##Checks if the orginal string is equal to reversed string 
        if encode_string == encode_string[::-1]:                  ##If the string is the same as it is revered 
            len_encode = len(encode_string)                       ##Then check the len of str
            if len_encode > largest_length:                       ##if the len of encode is greater than len of largest len
                largest_length = len_encode                       ##then the largest len is going to equal the new largest len
                                                                  
print(largest_length)                                             ##Print out the largest len
