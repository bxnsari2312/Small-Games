##Bansari Shah
##ICS4U-C
##J3 - 2013; 1987 to 2013
##02/20/2022

##get input for the start year
start_year = int(input())

##Set initial double to true
double = True

##Create a while loop until double truns flase
while (double == True):
    ##start by adding additional year
    start_year += 1
    ##check if there is any repeat using the set function;
    ##If there is break the loop
    if ((len(set(str(start_year))) < len(str(start_year))) == False):
        break
##print the end year
print(start_year)


##How does the set function work:
##Example start_year = 1001
    ##len(set(str(start_year))):
    ##1. convert the int to str; make it iterable
    ##2. convert the str to a set; possible because it is iterble; in set: "1", "0", "0", "1"
    ##3. len(set()); gives the number of unique digits inside the set
        ##In the top code we compared: if the number of unqiue digits is less than the len str
        ##if it is less than the len then there are repeats; else; no repeats 

