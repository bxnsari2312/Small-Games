#Bansari Shah
#ICS3U0
#Waterloo J3; 2010
#29 Oct 2020

A = 0
B = 0

store_list = []
while True:
    data = input()
    if data == "7":
        break
    else:
        store_list.append(data)
        
    for index in range(len(store_list)):
        if store_list[index][0] == "1":
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


