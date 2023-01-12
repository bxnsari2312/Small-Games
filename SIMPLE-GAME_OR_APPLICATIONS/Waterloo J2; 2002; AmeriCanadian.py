#Bansari Shah
#ICS3U0
#Waterloo J2; 2002
#21 Oct 2020

while True:
    word = input()

    if word == "quit!":
        break

    if (len(word) > 4) and (word.endswith("or")):
        word = word.replace("or", "our")
        
    print(word)

    
