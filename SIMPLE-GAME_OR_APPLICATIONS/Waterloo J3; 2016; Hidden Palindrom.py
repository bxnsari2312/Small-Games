#Bansari Shah
#ICS3U0
#Waterloo J3; 2016
#27 Oct 2020

string = input()
largest_length = ""
length  =[]

##Need to use len(strung)+1 for slicing
for counter in range(len(string)+1):
    for index in range(counter, len(string)+1):
        encode_string = string[counter:index]
        ##Checks if the orginal string is equal to reversed string
        if encode_string == encode_string[::-1]:
            len_encode = len(encode_string)
            if len_encode > largest_length:
                largest_length = len_encode
print(largest_length)
                
