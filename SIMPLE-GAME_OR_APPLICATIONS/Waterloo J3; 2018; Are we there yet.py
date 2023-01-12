#Bansari Shah
#ICS3U0
#Waterloo J2; 2018
#22 Oct 2020


distance = input().split()

for counter in range(4):
    distance[counter] = int(distance[counter])
    
location = [0]
##First find all the location of cities
for count in range(4):
    ##You add proir city and its same distance
    location.append(location[count]+distance[count])

##Now since we locations of cities, we need distance between any two cities
for each_city in range(5):
    results = []
    ##Now comparing each location to 
    for city in range(5):
        distances = location[city] - location[each_city]
        if distances < 0:
            ##If distance is negative turn it into postive 
            distances = abs(distances)  
        results.append(distances)
    print(results)
    
