#Bansari Shah
#ICS3U0
#Waterloo J3; 2019
#26 Oct 2020

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
    compare = lists[string]
    store_compress = ""
    count = 1
    for chars in range(len(compare)):
        ##If chars is not at the last index of string
        if chars != (len(compare) - 1) and compare[chars] == compare[chars+1]:
            count += 1
        else:
            store_compress += " "+str(count)+ " " + compare[chars]
            count = 1
    print(store_compress[1:])
                
#################################################################################################

               
