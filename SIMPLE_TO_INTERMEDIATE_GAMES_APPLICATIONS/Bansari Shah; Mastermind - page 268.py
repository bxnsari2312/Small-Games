##Bansari Shah
##ICS4U0-C
##Mastermind; Pg 268
##02/15/2022

##Import the random funtion to generate random int
import random

##From user get the input for the num of pegs and the colour
##For the game; create var to store the answer and the guess; if the guess = answer, player wins
pegs = int(input("Enter the number of pegs (1-10): "))
col =  int(input("Enter the number of colours (1-9): "))
ans = ""
guess = ""

####From the given pegs and colour generate answer by randomly getting each char
##for num in range (pegs):
##    ans += str(random.randint(1, col))

ans = "123456"
    
##For checking purposes: can print out the answer beforehand 
print(ans)

##While the guess is not equal to answer
##Create empty guess str for each try
tries = 1
while guess != ans:
    guess = ""
    print("Guess " + str(tries) + ":")

##Enter guesses for the each num of pegs
    for num_peg in range(pegs):
        guess += input("colour for peg: ")
    print(guess)

##count the numbers of colours which are correct by comparing two strings 
    count_col = 0
    ##set funtion creates a common set; then create a common list which has ans AND guess; then count
    common = list(set(ans) and set(guess))
    print (common)
    for i in common:
        count_col += 1
        

##count the numbers of peg postion correct by comparing the index of two strings
    count_peg = 0
    for cor in range (0, len(guess), 1):
        if (guess[cor] == ans[cor]):
            count_peg += 1

    print("You have " + str(count_peg) + " peg correct and " + str(count_col) + "colour(s) correct.")
    ##start next try; reset the count_col and count_peg to check again
    tries += 1
    count_col = 0
    count_peg = 0
    
print("You have broken the code in" + str(tries) + "guesses")
    
