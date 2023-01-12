#Bansari Shah
#ICS3U0
#Waterloo J3; 2020
#22 Oct 2020


Num_drops = int(input())
x_values = []
y_values = []

for data in range(Num_drops):
    data = input()
    x, y = data.split()
    x = int(x)
    y = int(y)
    x_values += [x]
    y_values += [y]

min_y = min(y_values)
min_x = min(x_values)
max_y = max(y_values)
max_x = max(x_values)

new_min_x = min_x - 1 ##So it shifts more to the left
new_min_y = min_y - 1 ##So it shifts more down

new_max_x = max_x + 1 
new_max_y = max_y + 1

print(new_min_x, new_min_y)
print(new_max_x, new_max_y)





    
    
    
    
    
    
