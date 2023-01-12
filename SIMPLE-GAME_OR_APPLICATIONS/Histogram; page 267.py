#Bansari Shah
#ICS3U0
#Analyze And Histogram; page 267
#31 Oct 2020


ranges = []
for numbers in range(10):
    ranges.append(0)
ranges_val = ["1 - 5:","6 - 10:","11 - 15:","16 - 20:","21 - 25:", "26 - 30:", "31 - 35:", "36 - 40:", "41 - 45:", "46 - 50:"]

while True:
    number = int(input("Enter num 1-50, enter -1 to quit: "))
    if number == -1:
        break
    if (1<= number <= 5):
        ranges[0] += 1
    elif(6<= number <= 10):
        ranges[1] += 1
    elif(11<= number <= 15):
        ranges[2] += 1
    elif(16<= number <= 20):
        ranges[3] += 1
    elif(21<= number <= 25):
        ranges[4] += 1
    elif(26<= number <= 30):
        ranges[5] += 1
    elif(31<= number <= 35):
        ranges[6] += 1
    elif(36<= number <= 40):
        ranges[7] += 1
    elif(41<= number <= 45):
        ranges[8] += 1
    elif(45<= number <= 50):
        ranges[9] += 1

for index in range(len(ranges)):
    print("{0:>10s} {1:s}".format(ranges_val[index], ("*"*(ranges[index]))))
