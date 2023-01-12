#Bansari Shah
#ICS3U0
#Question 1; Test Loops and Strings
#23 Oct 2020

##Get user input as a string
user_data = input()     

 ##Use the string count function to check how many happy faces ##present 
count_happy = user_data.count(":-)")   
   
##Use the string count function to check how many sad faces present 
count_sad = user_data.count(":-(")       

##If there are 0 happy and sad faces 
if (count_happy == 0) and (count_sad == 0):  
 ##Then print none
    print("none")          
##If there are equal number of happy and sad faces                   
elif(count_happy == count_sad):       
 ##Print unsure; user is unsure       
    print("unsure")           
 ##If there are more happy faces                
elif(count_happy > count_sad):    
##Print happy, user is happy           
    print("happy")   
##Else the user is sad, that is the only option left                      
else:
    print("sad")        
