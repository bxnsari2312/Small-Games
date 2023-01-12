##Bansari Shah
##ICS3U0
##Waterloo J4; 2004
##06 Nov 2010

key = input()
message = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message_list = []
shifts = []
blocks = []

for letter in message:
    if letter in alphabet:
        message_list.append(letter)

for shift in key:
    shifts.append(alphabet.index(shift))

##for loop starts at 0, ends at last letter of message, goes step by length of key
for block in range(0, len(message), len(key)):
    ##starts at block, and goes to until the len of key
    ## B A N A N A P E E L
    ##block = 0; [0:3]
    ##block = 3; [3:6]
    ##block = 6; [6:9]
    blocks.append(message_list[block:block+len(key)])

for i in range(len(blocks)):
    for index in range(len(blocks[i])):
        ##Captical ord from A to Z
        if (65 <= ord(blocks[i][index]) <= 90):
            (blocks[i][index]) = (ord(blocks[i][index]) +  shifts[index])

            if (blocks[i][index] > 90):
                (blocks[i][index]) = ((blocks[i][index])-90)+64

for Print in range(len(blocks)):
    for Printing in range(len(blocks[Print])):
        blocks[Print][Printing] = chr(blocks[Print][Printing])
        print(blocks[Print][Printing], end = "")
                
            
        
    
    
    


        

