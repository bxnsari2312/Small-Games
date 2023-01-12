##Bansari Shah
##ICS4U-C
##J3 - 2004; Smile with similes
##02/20/2022

##Enter the adjectives and the nouns 
num_adjectives = int(input())
num_nouns = int(input())

##create list for the adjectives and nouns
adjectives = []
nouns = []


##for num of adj; take adjective as input and append to list
for num in range(num_adjectives):
    adjective = input()
    adjectives.append(adjective)
##for num of nouns; take nouns as input and append to list
for num in range(num_nouns):
    noun = input()
    nouns.append(noun)

##Create nested loop to match up the adjectives and nouns 
for printing in range(len(adjectives)):
    for prints in range(len(nouns)):
        print(adjectives[printing], "as", nouns[prints])

