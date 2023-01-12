#Bansari Shah
#ICS3U0
#Metric Conversion; Page 175
#06 Nov 2020

def inches_to_cm(inches):
    cm = inches*2.54
    return cm

def feet_to_cm(feet):
    cm = feet*30
    return cm

def yards_to_meters(yards):
    meters = yards*0.91
    return meters

def miles_to_kilometers(miles):
    kilometers = miles*1.6
    return kilometers

def cm_to_inches(cm):
    inches = cm/2.54
    return inches

def cm_to_feet(feet):
    feet = cm/30
    return feet

def meter_to_yard(meter):
    yard = meter/0.91
    return yard

def kilometers_to_miles(kilometers):
    miles = kilometers/1.6
    return miles

one_four = ["1.", "2.", "3.", "4."]
one_four_choices = ["inches to centimeters", "Feet to centimeter", "Yards to meters", "Miles to kilometers"]
five_eight = ["5.", "6.", "7.", "8."]
five_eight_choices = ["centimeter to inches", "centimter to feet", "meters to yards", "kilometers to miles"]

number = int(input("Enter a number: "))
print("Convert")

for printing in range(len(one_four)):
    print(one_four[printing], one_four_choices[printing], "{0:>20s} {1:10s}".format(five_eight[printing],five_eight_choices[printing]))

choice = int(input("Enter choice: "))
if choice == 1:
    answer = inches_to_cm(number)
elif choice == 2:
    answer = feet_to_cm(number)
elif choice == 3:
    answer = yards_to_meters(number)
elif choice == 4:
    answer = miles_to_kilometers(number)
    
print(answer)
    



























