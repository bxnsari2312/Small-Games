##Bansari Shah
##ICS4U0-C
##Big Bang - J4 2012
##02/10/2022


##Given: The inputted code is shifted by ##S = 3P+k
##Enter the shift value, and the word
##Create a str var to store the final output 
shift_k = int(input())
word = input()
new = ""

##Create a for loop to analyze each character 
for letter in range (len(word)):

    ##Check if the word is within the range of "A" to "Z"
    if (65 <= ord(word[letter]) <= 90):
        
        ##Neg S: because we are decoding; need to do opposite of addition which is subtraction
        S = -1*((3*(letter+1))+shift_k)
        ##We create a new shift value for the shifted char
        new_shift_value = ord(word[letter])+S

        ##If new code is within the range: add to chars to final str to be outputted 
        if (65 <= new_shift_value <= 90):
            new += (chr(new_shift_value))

        ##If it goes beyond range of "A" - "Z": subtract 26 (total letters of the alphabet to shift back) and then add char final str to be outputted
        elif (new_shift_value > 90):
            new_shift_value = (new_shift_value-26)
            new += (chr(new_shift_value))

        ##If it goes below range of "A" - "Z": add 26 (total letters in the alphabet to shift down) and then add final str to be outputted
        elif (new_shift_value < 65):
            new_shift_value = 26 + new_shift_value
            new += (chr(new_shift_value))
            
    ##Else, if it is not part of the alphabet then print out the inputted char 
    else:
        new += (chr(letter))

##Print final inputted code      
print(new)
            
            
