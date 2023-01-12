#Bansari Shah
#ICS3U0
#Waterloo J2; 2001
#21 Oct 2020

x = int(input("Enter x: "))
m = int(input("Enter m: "))

for num in range(1, m+1, 1):
    if (x * num) % m == 1:
        print(num)
        break
