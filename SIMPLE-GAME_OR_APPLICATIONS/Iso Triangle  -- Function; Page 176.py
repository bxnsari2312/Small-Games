#Bansari Shah
#ICS3U0
#Iso Triangle; Page 176
#06 Nov 2020

number = int(input("Enter the size: "))

def addSpaces(size):
    spaces = []
    for i in range(size):
        size -= 1
        spaces.append(" "*(size))
    return spaces

def drawBar(size):
    star = 1
    stars = ["*"]
    for i in range(size-1):
        star += 2
        stars.append("*"*star)
    return stars

space = addSpaces(number)
star = drawBar(number)

for i in range(len(space)):
    print(space[i] + star[i] + space[i])
    
        
    
        
    

