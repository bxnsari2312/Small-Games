##Bansari Shah
##ICS4U-C
##J3 - 2006; Cell-Phone Messaging
##02/20/2022

##Added extra zero, so index value is the button value 
positions = ["0","adgjmptw", "behknqux", "cfilorvy", "sz"]
##added extra zeros infront so index val us the button val 
button = ["0", "0", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

words = []
words_count = []

def time_pause(words):
    for indexs in range(len(words)):
        for char in range(len(words[indexs])):
            if any((words[indexs][char]) in word for word in positions):
                words_count[indexs] += (positions.index(word[char] in positions))

    if (char != (len(words[indexs])-1)):
        if (words[indexs][char] == (words[indexs][char+1])):
            words_count[indexs] += 2

    return(words_count)

while True:
    word = input()
    if word == "halt":
        break

    words.append(word)
    words_count.append(0)
    time_pause(words)
print(word_count)

