#Bansari Shah
#ICS3U0
#Waterloo J2; 2016
#18 Oct 2020

user_data = input()

count_happy = user_data.count(":-)")
count_sad = user_data.count(":-(")

if (count_happy == 0) and (count_sad == 0):
    print("none")
elif(count_happy == count_sad):
    print("unsure")
elif(count_happy > count_sad):
    print("happy")
else:
    print("sad")
