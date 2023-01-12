##Bansari Shah
##ICS4U0-C
##J4 2021; Arranging Books
##02/17/2022

##Large, Medium, Small

##Solution Steps:
##1. count the number of L, M, S
##2. divide into three sections based on size; and count how many of them are in correct position
##3. starting from the largest section; swap the books from the largest section to the smalled
##4. Count the amount of effeicent swaps; min(L's in M, M's in L) --> moves saved from making efficeint swaps 
##5. swap out all non-M's out of n section -- > only the S remains in the S section
##6. Total_num swaps = (#non-L's in L section + #non-M's in M section - min(L's in M, M's in L))


##Create a class for each section: defining particular type of object
class section:
    l = 0
    m = 0
    s = 0

    ##create a initailize a function which looks at seach book in the self and returns the type of book
    def initials (self):
        self.l = 0
        self.m = 0
        self.s = 0

    ##create a initailize a function which looks at seach book in the self and returns the type of book
    def move(self, book):
        if (book == "L"):
            self.l += 1
        if (book == "S"):
            self.s += 1
        if (book == "M"):
            self.m += 1

##take in books input
books = input()
#Counts L, M, S books in total
total = section()

##Loops through each books and counts 
for num_book in books:
    total.move(num_book)

##Three section classes/ objects; for three size 
l = section()
m = section()
s = section()

##Set inotail j val to 0
j = 0
##In the L section counts the L, M, S books
##Will run total 1 times; because there would be total of L books in large section
for i in range(total.l):
    l.move(books[j])
    j += 1
##In the M section counts the L, M, S books 
for i in range(total.m):
    m.move(books[j])
    j += 1
##In the S section counts the L, M, S books 
for i in range(total.s):
    s.move(books[j])
    j += 1

##number of non-L's + non-M's - efficeint swap (common of M and L)
print(l.m + l.s + m.l + m.s - min(m.l, l.m))


        
        
