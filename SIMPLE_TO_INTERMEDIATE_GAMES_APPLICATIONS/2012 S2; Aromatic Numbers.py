##Bansari Shah
##ICS4U-C
##2012 S2: Aromatic Numbers
##05/01/2022

def roman(x):
    if x == "I":
        num = 1
    elif x == "V":
        num = 5
    elif x == "X":
        num = 10
    elif x == "L":
        num = 50
    elif x == "C":
        num = 100
    elif x == "D":
        num = 500
    else:
        num = 1000
    return num

file = open("s2.2.txt", "r")
aromatic = file.readline().strip()
oldr = 999999
olds = 0
value = 0

for i in range(len(aromatic), 2):
    a = eval(aromatic[i:i+1])
    r = roman(aromatic[i+1:i+2])
    s = a*r
    value += s
    if r > oldr:
        value -= 2*olds
    olds = s
    oldr = r
print(value)


