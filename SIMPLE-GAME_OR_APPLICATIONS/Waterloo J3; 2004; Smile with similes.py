##Bansari Shah
##ICS3U0
##Waterloo J3; 2004
##2 Nov 2020

num_adjectives = int(input())
num_nouns = int(input())

adjectives = []
nouns = []

for num in range(num_adjectives):
    adjective = input()
    adjectives.append(adjective)

for num in range(num_nouns):
    noun = input()
    nouns.append(noun)

for printing in range(len(adjectives)):
    for prints in range(len(nouns)):
        print(adjectives[printing], "as", nouns[prints])
