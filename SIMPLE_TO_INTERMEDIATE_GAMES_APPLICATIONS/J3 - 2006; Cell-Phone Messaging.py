##Bansari Shah
##ICS4U-C
##J3 - 2006; Cell-Phone Messaging
##02/20/2022

##TYpe up all the pauses 
first_pos = "adgjmptw"
second_pos = "behknqux"
third_pos = "cfilorvy"
fourth_pos = "sz"
##Type up all the postions of letters 
two = "abc"
three = "def"
four = "ghi"
five = "jkl"
six = "mno"
seven = "pqrs"
eight = "tuv"
nine = "wxyz"

##Create two lists; one for the words and other for the count
words = []
words_count = []

##Create a while loops until the word is halt
while True:
    word = input()
    if word == "halt":
        break
    
    words.append(word)                                  ##If no halt; append the word 
    words_count.append(0)                               ##append 0; to set initial count of that word 

for index_word in range(len(words)):                    ##consider each word in list
    for char in range(len(words[index_word])):          ##nested loop; consider each char in word 
        if words[index_word][char] in first_pos:        ##check each postion of the char and based on pos add time (s)
            words_count[index_word] += 1 
        elif words[index_word][char] in second_pos:
            words_count[index_word] += 2
        elif words[index_word][char] in third_pos:
            words_count[index_word] += 3
        elif words[index_word][char] in fourth_pos:
            words_count[index_word] += 4
            
        #As long as the char at index is not the last letter; consider the cbar 
        if char != len(words[index_word])-1:
            ##check if the word and the following are in the same letter; if so then add two secs
            if (words[index_word][char] in two) and (words[index_word][char+1] in two) or (words[index_word][char] in three) and \
               (words[index_word][char+1] in three) or (words[index_word][char] in four) and (words[index_word][char+1] in four) \
               or (words[index_word][char] in five) and (words[index_word][char+1] in five) or (words[index_word][char] in six) \
               and (words[index_word][char+1] in six) or (words[index_word][char] in seven) and (words[index_word][char+1] in seven)\
               or (words[index_word][char] in eight) and (words[index_word][char+1] in eight) or (words[index_word][char] in nine) \
               and (words[index_word][char+1] in nine):

                words_count[index_word] += 2

for results in range(len(words_count)):              ##Print each counted word 
    print(words_count[results])



