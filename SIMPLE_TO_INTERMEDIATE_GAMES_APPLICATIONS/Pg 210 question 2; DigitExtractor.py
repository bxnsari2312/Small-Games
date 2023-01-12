##Bansari Shah
##ICS4U-C
##Pg 210 #2; DigitExtractor
##04/06/2022

class Num:

    def __init__(self, num):
        self.whole = num
        self.hundreds = 0
        self.tens = 0
        self.ones = 0

    def show_h(self, num):
        self.hundreds = num[0]
        ansh = ("hundreds place digit is: " + self.hundreds)
        return ansh
       
    def show_t(self, num):
        self.tens = num[1]
        anst = ("tens place digit is: " + self.tens)
        return anst

    def show_o(self, num):
        self.ones = num[2]
        anso = ("ones place digit is: "+self.ones)
        return  anso

    def __repr__(self):
        data = str(self.whole)
        return data


while True:
    ints = input("Enter an integer: ")
    choice = input("Enter your choice: ")
    num = Num(ints)
    
    if choice == "Q":
        break

    if (choice == "W"):
        print(nums)
    elif(choice == "O"):
        print(num.show_o(ints))
    elif(choice == "T"):
        print(num.show_t(ints))
    elif(choice == "H"):
        print(num.show_h(ints))
        
        
        


