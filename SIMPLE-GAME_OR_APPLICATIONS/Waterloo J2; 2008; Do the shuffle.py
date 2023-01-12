#Bansari Shah
#ICS3U0
#Waterloo J2; 2014
#18 Oct 2020

##playlist = ["A", "B", "C", "D", "E"]

##Button 1
##playlist.insert(len(playlist), playlist[0])
##playlist.remove(playlist[0])
##print(playlist)

##Button 2
##temp = playlist[-1]
##playlist.remove(playlist[-1])
##playlist.insert(0, temp)
##print(playlist)

##Button 3
##Temp = playlist[0]
##playlist[0] = playlist[1]
##playlist[1] = Temp
##print(playlist)
#########################################################################

playlist = ["A", "B", "C", "D", "E"]
while True:
    Button = int(input("Button Number: "))
    Press = int(input("Number of Presses: "))
    if Button == 1:
        for shuffle in range(Press):
            playlist.insert(len(playlist), playlist[0])
            playlist.remove(playlist[0])
    elif Button == 2:
        for shuffle in range(Press):
            temp = playlist[-1]
            playlist.remove(playlist[-1])
            playlist.insert(0, temp)
    elif Button == 3:
        for shuffle in range(Press):
            Temp = playlist[0]
            playlist[0] = playlist[1]
            playlist[1] = Temp
    else:
        break
print(playlist)
            
            
        
            
            
            
            
            
            
    
