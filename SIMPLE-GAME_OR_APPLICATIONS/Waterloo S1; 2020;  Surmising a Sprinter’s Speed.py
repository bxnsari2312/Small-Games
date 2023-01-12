##Bansari Shah
##ICS3U0
##S1 2020;Surmising a Sprinter’s Speed
##13 Nov 2020

All_Time = []
All_Travelled = []
speeds = []

num_lines = int(input())


def cal_speed(time, distance):
    speed = abs(distance / time)
    return speed 

for i in range(num_lines):
    Time, Distance = input().split()
    All_Time.append(int(Time))
    All_Travelled.append(int(Distance))

for i in range(num_lines):
    for u in range(i):
        X = abs(All_Travelled[i]-All_Travelled[u])
        T = abs(All_Time[i]-All_Time[u])
        speeds.append(cal_speed(T, X))

print(max(speeds))
        
        
        
    
