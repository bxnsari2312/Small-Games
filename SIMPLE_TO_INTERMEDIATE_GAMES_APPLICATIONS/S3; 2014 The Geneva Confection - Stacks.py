##Bansari Shah
##ICS4U-C
##S3; 2014 The Geneva Confection - Stacks
##05/26/2022

##Logic:
##get the number of test cases; each test has first input asking for the number of cars
##  use for loop to get the test case data
##for each test:
##  convert the user data into a lst and use the pop method to implement stacks
##  if the number at end of the lst is greater than number prior pop it and add to branch, else,
##  check the next index
##condition for branch: if the number in lst are not ascending order; the test fails 


def check_ascending(lst):
    flag = False
    for i in range(len(lst)-1):
        if flag == True:
            break
        if lst[i] > lst[i+1]:
            flag = True
            break
    return flag

test_cases = int(input())
answers = []
for tests in range(test_cases):
    num_cars = int(input())
    car_lst = [int(input())for i in range(num_cars)]
    branch = []

    for n in range(len(car_lst)-1, -1, -1):
        if n > 0:
            if (car_lst[n] > car_lst[n-1]):
                branch.append(car_lst[n])
                car_lst.pop(n)
    if check_ascending(branch) == True:
        answers.append("Y")
    else:
        answers.append("N")

for data in answers:
    print(data)




