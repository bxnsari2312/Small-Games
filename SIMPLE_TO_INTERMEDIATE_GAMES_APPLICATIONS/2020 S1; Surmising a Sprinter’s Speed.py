##Bansari Shah
##ICS4U-C
##2020 S1: Surmising a Sprinter’s Speed
##05/01/2022

##max speed is the avg between the first and last points
n = int(input())
speed_data = []

for i in range(n):
    data = input().split()
    data = [int(x) for x in data]
    speed_data.append(data)

speed_data.sort()
print(speed_data)

initial_speed = 0
for i in range(n):
    time_diff = speed_data[i][0] - speed_data[i - 1][0]
    dist_diff = abs(speed_data[i][1] - speed_data[i - 1][1])
    speed = (dist_diff / time_diff)

    if speed > initial_speed:
        initial_speed = speed
        
        
print(initial_speed)


    



    




