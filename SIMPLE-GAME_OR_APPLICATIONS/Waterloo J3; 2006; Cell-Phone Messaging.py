##Bansari Shah
##ICS3U0
##Waterloo J3; 2006
##1 Nov 2020

first_pos = "adgjmptw"
second_pos = "behknqux"
third_pos = "cfilorvy"
fourth_pos = "sz"
two = "abc"
three = "def"
four = "ghi"
five = "jkl"
six = "mno"
seven = "pqrs"
eight = "tuv"
nine = "wxyz"

words = []
words_count = []

while True:
    
    word = input()
    if word == "halt":
        break
    
    words.append(word)
    words_count.append(0)

for index_word in range(len(words)):
    for char in range(len(words[index_word])):
        if words[index_word][char] in first_pos:
            words_count[index_word] += 1
        elif words[index_word][char] in second_pos:
            words_count[index_word] += 2
        elif words[index_word][char] in third_pos:
            words_count[index_word] += 3
        elif words[index_word][char] in fourth_pos:
            words_count[index_word] += 4
            
        #As long as the char at index is not the last letter
        if char != len(words[index_word])-1:

            if (words[index_word][char] in two) and (words[index_word][char+1] in two) or (words[index_word][char] in three) and \
               (words[index_word][char+1] in three) or (words[index_word][char] in four) and (words[index_word][char+1] in four) \
               or (words[index_word][char] in five) and (words[index_word][char+1] in five) or (words[index_word][char] in six) \
               and (words[index_word][char+1] in six) or (words[index_word][char] in seven) and (words[index_word][char+1] in seven)\
               or (words[index_word][char] in eight) and (words[index_word][char+1] in eight) or (words[index_word][char] in nine) \
               and (words[index_word][char+1] in nine):

                words_count[index_word] += 2

print(words_count)
for results in range(len(words_count)):
    print(words_count[results])



