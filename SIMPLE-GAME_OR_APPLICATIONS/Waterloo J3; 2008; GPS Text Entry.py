#Bansari Shah
#ICS3U0
#Waterloo J3; 2009
#29 Oct 2020

word = input()
full_word = "A"+word+"e"
key_board_x = ["ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZ -.e"]
key_board_y = ["AGMSY", "BHNTZ", "CIOU ", "DJPV-", "EKQW.", "FLRXe"]

steps = 0
x = 0
y = 0
coordinates = []

for counter in range(len(word)):
    char = word[counter]
    for index in range(len(key_board_x)):
        if char in key_board_x[index]:
            ##Added one extra for the A
            x = index + 1
    for index in range(len(key_board_y)):
        if chars in key_board_y[index]:
            y = index + 1
    coordinates.append((x,y))

for index in range(len(coordinates)):
    steps += abs(coordinates[index+1][0] - coordinates[index][0])
    steps += abs(coordinates[index+1][1] - coordinates[index][0])
print(steps)
            
