##Bansari Shah
##ICS4U-C
##Dictionaries Exercise 13.3
##05/11/2022

##dictionary: {book_num:[firstname, lastname, tittle]}

##num_books = int(input("Enter the number of books: "))
##lib = {"location_num":"information"}
##
##for i in range(num_books):
##    book = input("Enter location num: ")
##    book_info = input("Enter FN, LN, TITTLE").split()
##    lib[book] = book_info
##
##author = input("Enter author name: ")
##result = [lib[author] for x in order_list]


###################################################################################################################

num_books = int(input("Enter the number of books: "))
lib = {"location_num":"information"}

for i in range(num_books):
    book = input("Enter author: ")
    book_info = input("Enter TITTLE, LOCATION: ").split()
    lib[book] = book_info

author = input("Enter author name: ")
result = [lib[author][2] for author in lib]
print(result)
