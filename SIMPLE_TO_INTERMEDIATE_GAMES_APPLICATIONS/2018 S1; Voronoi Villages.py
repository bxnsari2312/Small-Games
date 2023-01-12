##Bansari Shah
##ICS4U-C
##2018 S1: Voronoi Villages
##05/01/2022

num_vil = int(input())
points = [int(input()) for i in range(num_vil)]
points.sort()

left = 0
right = 0

smallest = 1000000

for i in range(1, num_vil-1):
    leftdiff = points[i] - points[i - 1]
    left = leftdiff / 2
    rightdiff = points[i + 1] - points[i]
    right = rightdiff / 2

    if (left + right < smallest):
        smallest = left + right

print("%.1f" % smallest)
