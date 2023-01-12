##Bansari Shah
##ICS4U-C
##J3 - 2019; Cold Compress
##02/17/2022

##Int input; total num of lines for input
num_lines = int(input())
##New list where all inputs are converted to one list
lists = []

##For num of lines; ask for that many string input
for num in range(num_lines):
    ##append/add all inputs to single list called "lists"
    lists.append(input())


##goes through the largest index
for string in range (len(lists)):
    ##consider a whole statement
    compare = lists[string]
    ##Set initial store_compress to ""
    store_compress = ""
    ##set initial count = 1; because initially one of char is present 
    count = 1
    ##consider individual char of the statement
    for chars in range(len(compare)):
        ##If chars is not at the last index of string; if there is not a single char and if it is equal to val at next index
        ##Check if its not the last letter AND check if the next one is equal to the one before 
        if (chars != (len(compare) - 1)) and (compare[chars] == compare[chars+1]):
            ##Add a count 
            count += 1
        ##else; if the char is not repeated then it storees the count and the char 
        else:
            store_compress += (" "+str(count)+ " " + compare[chars])
            count = 1
    ##Print out the value of each index; [1:] format to get rid of extra space  
    print(store_compress[1:])


