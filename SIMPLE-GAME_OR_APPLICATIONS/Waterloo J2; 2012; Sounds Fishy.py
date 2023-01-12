#Bansari Shah
#ICS3U0
#Waterloo J2; 2012
#18 Oct 2020

data1 = int(input())
data2 = int(input())
data3 = int(input())
data4 = int(input())

if(data1 < data2 < data3 < data4):
    print("Fish Rising")
elif(data1 > data2 > data3 > data4):
    print("Fish Diving")
elif(data1 == data2 == data3 == data4):
    print("Constant Depth")
else:
    print("No Fish")
    
