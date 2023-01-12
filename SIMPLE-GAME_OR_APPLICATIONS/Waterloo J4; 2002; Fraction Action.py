##Bansari Shah
##ICS3U0
##Waterloo J4; 2002
##06 Nov 2020

Numerator = int(input("Numerator: \n"))
Denominator = int(input("Denominator: \n"))

whole = (Numerator // Denominator)
fraction_num = (Numerator % Denominator)
fraction_den = Denominator

num1 = fraction_num
num2 = fraction_den

##Euclids algorithm to find the greatest common divisor
while (num2 != 0):
    temp1 = num1
    num1 = num2
    num2 = temp1 % num2
    
common_factor = num1

if common_factor != fraction_den:
    fraction_num = str(fraction_num // common_factor)
    fraction_den = str(fraction_den // common_factor)
    print("")
    print(whole, fraction_num+"/"+fraction_den)
else:
    print("")
    print(whole)




    
    



