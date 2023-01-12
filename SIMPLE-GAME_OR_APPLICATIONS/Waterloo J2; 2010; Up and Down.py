#Bansari Shah
#ICS3U0
#Waterloo J2; 2010
#18 Oct 2020

a = int(input("Give value for a: "))    ##NIKKY STEP FORWARD AT A TIME
b = int(input("Give value for b: "))    ##NIKKY STEP BACKWARD AT A TIME
c = int(input("Give value for c: "))    ##BYRON STEP FORWARD AT A TIME 
d = int(input("Give value for d: "))    ##BYRON STEP BACKWARD AT A TIME
s = int(input("Give value for s: "))    ##NUM STEPS TAKEN IN TOTAL 

nikky_distance = 0     ##NIKKY DISTANCE 
nikky_steps = 0        ##NIKKY STEPS TAKEN 
bryon_distance = 0     ##BYRON DISTANCE 
bryon_steps = 0        ##BYRON STEPS TAKEN 

directionA = 1         ##IF GOING FORWARD OR BACKWARDS; POS OR NEG
pattern = a            ##VALUE OF STEP FORWARD OR BACKWARD 

while nikky_steps < s:                          ##STEPS ARE LESS THAN TOTAL 
    nikky_distance += (directionA * pattern)     ##DISTANCE IS THE DIRECTION PLUS THE VALUE OF STEP
    nikky_steps += pattern                      ##TOTAL STEPS TAKEN SO FAR 
    if directionA == 1:                          ##TO CHANGE THE DIRECTION
        pattern = b                             ##NOW DIRECTION IS GOING BACK 
    else:
        pattern = a                             ##CHNAGE DIRECTION BACK TO FRONT
        directionA *= -1                             ##VALUE OF DIRECTION/ BACK AND FORTH CHNAGES BY MULTIPLYING BY ONE

directionB = 1
patternB = c
while bryon_steps < s:
    bryon_distance += (directionB * patternB)
    bryon_steps += patternB
    if directionB == 1:
        patternB = d
    else:
        patternB = c
    patternB *= -1

if bryon_distance > nikky_distance:
    print("Byron")
elif bryon_distance < nikky_distance:
    print("Nikky")
else:
    print("Tie")
    
 


    
        
    
    
