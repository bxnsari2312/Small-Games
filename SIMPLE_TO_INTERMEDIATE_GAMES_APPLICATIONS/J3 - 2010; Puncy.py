##Bansari Shah
##ICS4U-C
##J3 - 2010; Puncy
##02/20/2022

##import the math library to use function to round 
import math

##set inital values of a and b to zero
A = 0
B = 0
##Create a list to store all the answer data 
store_list = []

#Use a while loop for answering each questions
##Consider all 6 cases starting from 1-6 and print the following ans 
while True:
    data = input()                                  ##Get the data input
    if data == "7":                                 ##if user input is 7 then break
        break
    else:
        store_list.append(data)                     ##add data to the list
        
    for index in range(len(store_list)):            ##Consider the three cases for each index; 1, A, B
        if store_list[index][0] == "1":             ##If in the list; if the cuurent word; word at index 0 == 1
            if store_list[index][2] == "A":           
                    A = int(store_list[index][4])   
    
            elif store_list[index][2] == "B":
                    B = int(store_list[index][4])
    
        elif store_list[index][0] == "2":
            if store_list[index][2] == "A":
                print(A)
            elif store_list[index][2] == "B":
                print(B)
    
        elif store_list[index][0] == "3":
            if store_list[index][2] == "A":
                if store_list[index][4] == "B":
                    A = (A + B)
                elif store_list[index][4] == "A":
                    A = (A + A)
            elif store_list[index][2] == "B":
                if store_list[index][4] == "A":
                    B = (B + A)
                elif store_list[index][4] == "B":
                    B = (B + B)
                    
        elif store_list[index][0] == "4":
            if store_list[index][2] == "A":
                if store_list[index][4] == "B":
                    A = (A * B)
                elif store_list[index][4] == "A":
                    A = (A * A)
            elif store_list[index][2] == "B":
                if store_list[index][4] == "A":
                    B = (B * A)
                elif store_list[index][4] == "B":
                    B = (B * B)

        elif store_list[index][0] == "5":
            if store_list[index][2] == "A":
                if store_list[index][4] == "B":
                    A = (A - B)
                elif store_list[index][4] == "A":
                    A = (A - A)
            elif store_list[index][2] == "B":
                if store_list[index][4] == "A":
                    B = (B - A)
                elif store_list[index][4] == "B":
                    B = (B - B)

        elif store_list[index][0] == "6":
            if store_list[index][2] == "A":
                if store_list[index][4] == "B":
                    A = (A // B)
                elif store_list[index][4] == "A":
                    A = (A // A)
            elif store_list[index][2] == "B":
                if store_list[index][4] == "A":
                    B = (B // A)
                elif store_list[index][4] == "B":
                    B = (B // B)



