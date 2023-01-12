#Bansari Shah
#ICS3U0
#Waterloo J3; 2012


user_input = int(input())
star = "*"
x = "x"
spaces = " "

for count in range(user_input):
    print(star*user_input + x*user_input + star*user_input)

for count in range(user_input):
    print(spaces*user_input + x*user_input*2)

for count in range(user_input):
    print(x*user_input + spaces*user_input + x*user_input)

