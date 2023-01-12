##Bansari Shah
##ICS4U0-C
##Big Bang - J4 2012: Modified 
##02/10/2022

##Given that the code is shifted: S = 3P + k
##Input the shift amount and the coded word; create a new str to store the decode 
shift = int(input())
word = input()
decode = ""

##Check each letter in the string
for letter in range(len(word)):

    ##Decode the shift by doing the opposite of added; subtract, for each character 
    S = (-1)*((3 * (letter + 1)) + shift)
    new_shift = ord(word[letter]) + S

    ##If new shifted val is within the range of "A" - "Z": Add it to the final decode value 
    if (65 <= new_shift <= 90):
        decode += (chr(new_shift))

    ##The new shift value can not be greater than 90; because we are subtracting the shift
    ##Consider when the shift is below "A" value; add 26 (total num of alphabet) to go down on list
    ##Add decoded value to str to be outputted 
    elif (new_shift < 65):
        new_shift = 26 + new_shift
        decode += (chr(new_shift))

    ##Else, if inputted char is not a letter - then just keep that as output 
    else:
        decode += (chr(new_shift))
        
##Print out the final decoded value
print(decode)
