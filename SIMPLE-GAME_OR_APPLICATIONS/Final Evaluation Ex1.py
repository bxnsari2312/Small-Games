##Bansari Shah
##ICS3U0
##Final Evaluation Ex1 
##09 Nov 2020

##Number of lines of input
num_lines = int(input("Enter number of lines of text to encode: "))
##Answers of each of the lines of input would be stored here
list_of_all = []

##Funtion to find each encoded line; takes the parameter as inputed string 
def run_length_coder(user_input):
    ##Stores the answer of the encoded string for current input
    store_compress = ""
    ##Set count to one; the string at char of index always at least repeats once 
    count = 1
    ##For each char in the string 
    for char in range(len(user_input)):
        ##If the char is not the last char, and the char is the same one as the next char
        if ((char != (len(user_input)-1)) and (user_input[char] == user_input[char+1])):
            ##add one to count since the char is repeated 
            count += 1
        ##Else it breaks the same encode chain; 
        else:
            ##In the str store_compress join the repeated encoded str; write the count then the char was repeated
            store_compress += (" "+ str(count) + " " + user_input[char])
            ##Reset the count value to one for the check of the next part of string
            count = 1
    ##Return the store_compress string
    return store_compress

##For the number of lines
for num in range(num_lines):
    ##Ask the input labelled by the current times input is asked
    print("Enter text", str(num+1)+":", end = " ")
    text = input()
    ##Use the function run_length_coder to find the encoded string, and store it in list list_of_all
    list_of_all.append(run_length_coder(text))

##For the encoded strings in list_of_all print them 
for printing in range(len(list_of_all)):
    print(list_of_all[printing])

    

    
    
    
    
