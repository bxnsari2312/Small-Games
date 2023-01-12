##Bansari Shah
##ICS4U-C
##Dictionaries Exercise 13.1
##05/11/2022

##logic:
##get user input, and split the text into list of words
##for each word in the list count its occurance and remove all the occurance form list
##the count number is the value and the word it self is the key of the dictionary
##sort the dictionary out based on the key in alphabetical order
##print 



def removes (lst, val):
    return [value for value in lst if value != val]

user = input("Enter Text: ")
text = user.split()
d = {:}

for word in text:
    count = text.count(word)

    d[word] = count
    removes(text, word)

x = sorted(d.items())
print(x)


