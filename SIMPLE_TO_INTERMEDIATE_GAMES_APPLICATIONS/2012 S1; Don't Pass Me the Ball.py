##Bansari Shah
##ICS4U-C
##2012 S1: Don't pass me the ball! (DC)
##05/01/2022

##c(n,r) = n! / ((n-r)! * r!)
file = open("s1.5.txt", "r")
#n = eval(file.readline()) - 1
#print (n*(n-1)*(n-2))/6
for line in file:
    n = eval(line)
    n -= 1
print ((n*(n-1)*(n-2))/6)
