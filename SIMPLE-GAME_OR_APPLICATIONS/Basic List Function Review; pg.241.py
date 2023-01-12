#Bansari Shah
#ICS3U0
#Basic List Function Review; pg.241 
#27 Oct 2020

##Student_rooster
Num_students = int(input("Enter Number of students in class: "))
student_rooster = []
for data in range(Num_students):
    name = input("Enter student Name: ")
    student_rooster.append(name)
print("Student Rooster")
print(student_rooster)

#######################################################################
##Squares
squares_list = [1,2,3,4,5]
list_new = []
for num in range(len(squares_list)):
    answer = num ** 2
    list_new.append(answer)
    answer = 1
print(list_new)
#######################################################################
##Reverse
nums = []
for num in range(10):
    numbers = int(input("Enter nums 0-9 random: "))
    nums.append(num)
for i in range(10):
    nums[i] = i

print("Countdown")
count = []
for data in range(-1, (-1 - len(nums)), -1):
    count.append(nums[data])
print(count)
####################################################################
    

    
    
