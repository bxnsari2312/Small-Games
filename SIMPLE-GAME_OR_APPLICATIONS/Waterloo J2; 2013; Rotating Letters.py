#Bansari Shah
#ICS3U0
#Waterloo J2; 2013
#18 Oct 2020

rotate = ["I", "O", "S", "H", "Z", "X", "N"]
word = input()
count = 0

for chars in word:
    if chars in rotate:
        count += 1
if count == len(word):
    print("YES")
else:
    print("NO")
        
