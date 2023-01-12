##Bansari Shah
##ICS4U-C
##S2; 2014 Assigning Partners - Dictionaries 
##05/26/2022

##Logic:
#get the number of total people
#split the list of people at spaces
#create a dic for the students; two keys for two lines 
#based on index numbers create pairs; count that each pair occurs twice
#if pairs do not occur twice all conditions are not met (pattern); print - "bad"
##  else, print - "good"

#check the occurrence of each index at a list
def checks_counts(lst, length):
    flag = True 
    for i in range(length):
        counted = lst.count(lst[i])
        if flag == False:
            break
        if counted != 2:
            flag = False
            break
    return flag


num_people = int(input("Enter number of people: "))
group1 = input().split()
group2 = input().split()

students = {"group1":group1, "group2":group2}
pairs = []

for i in range(num_people):
    pair = (students["group1"][i], students["group2"][i])
    pair = sorted(pair)                                    ##sort the pair before checking its equal
    pairs.append(pair)

counts = checks_counts(pairs, num_people)
if counts == False:
    print("bad")
else:
    print("good")
    

    
