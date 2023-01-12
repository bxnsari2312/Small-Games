#Bansari Shah
#ICS3U0
#Coder; page 269
#27 Oct 2020

string = input("Enter a string: ")
new = []
for chars in range(len(string)):
    if string[chars] != " " or string[chars] != "x" or string[chars] != "y":
        new_char = (ord(string[chars]) + 2)
        new_char = chr(new_char)
        new += str(new_char)
    elif string[chars] == " ":
        new += " "
    elif string[chars] == "x":
        new += "a"
    elif string[chars] == "y":
        new += "b"

result = " ".join(new)
print(result)

##############################################################
##Get the input string 
string = input("Enter a string: ")
##Create a new string for new string being formed
new = ""
##Enter the num of desired shifts in the alphabet 
shift = int(input("Enter Shift: "))
##For loop is going to check each index in the string 
for chars in range(len(string)):
    ##If the index is not a space, or chars x and y 
    if string[chars] != " " or string[chars] != "x" or string[chars] != "y":
        ##New char is going to take the ord of string and add it by the shift value
        new_char = (ord(string[chars]) + shift)
        ##Then convert the shift value to letters
        new_char = chr(new_char)
        ##Add the new letter to the string 
        new += str(new_char)
    ##elif if the strinf is a space just add a space to new 
    elif string[chars] == " ":
        new += " "
    ##elif its the char "X" replace it with "a", add to new 
    elif string[chars] == "x":
        new += "a"
    ##Elif its the char "y" replace it with "b", add to new 
    elif string[chars] == "y":
        new += "b"

##Print final string 
print(new)
















