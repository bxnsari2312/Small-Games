#Bansari Shah
#ICS3U0
#Waterloo J2; 2006
#18 Oct 2020

m = int(input("Enter m: "))
n = int(input("Enter n: "))
count = 0

for integers in range(1, m+1):
    for numbers in range(1, n+1):
        if integers + numbers == 10:
            count += 1
print("There are",count,"ways to get the sum 10")
        
        
