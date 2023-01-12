##Bansari Shah
##ICS4U-C
##Pg 210 #1; MySavings
##04/06/2022


class PiggyBank:

    def __init__(self):
        self.penny = 0
        self.dime = 0
        self.nickel = 0
        self.quarter = 0
        self.total = 0
        self.takeout = []

    def show_bank(self):
        return (self.total)

    def add_penny(self, add_penny):
        self.penny += add_penny
        self.total += (0.01*add_penny)

    def add_dime(self, add_dime):
        self.dime += add_dime
        self.total += (0.10*add_dime)

    def add_quarter(self, add_quarter):
        self.quarter += (add_quarter)
        self.total += (0.25 * add_quarter)

    def add_nickel(self, add_nickel):
        self.nickel = add_nickel
        self.total = (0.05 * add_nickel)

    def take_money(self, amount):
        if (self.bank > amount):
            self.takeout = []
            self.total -= amount 
            if (amount > 0):
                q_takeout = (amount // self.quarter*0.25)
                if ((amount//(self.quarter*0.25)) > self.quarter):
                    q_takeout = self.quarter
                self.takeout.append([0.25, q_takeout])
                amount -= (self.quarter*0.25)


            if (amount > 0):
                p_takeout = (amount // self.penny*0.01)
                if ((amount//(self.penny*0.01)) > self.penny):
                    p_takeout = self.penny
                self.takeout.append([0.01, p_takeout])
                amount -= (self.penny*0.01)

            if (amount > 0):
                d_takeout = (amount // self.dime*0.10)
                if ((amount//(self.dime*0.10)) > self.dime):
                    d_takeout = self.dime
                self.takeout.append([0.10, d_takeout])
                amount -= (self.dime*0.10)

            if(amount > 0):
                n_takeout = (amount // self.nickel*0.05)
                if ((amount//(self.nickel*0.05)) > self.nickel):
                    n_takeout = self.nickel
                self.takeout.append([0.05, n_takeout])
                amount -= (self.nickel*0.05)

            return self.takeout

    def __repr__(self):
        data = ["penny: " + str(self.penny), "dime: "+str(self.dime), "nickel: "+str(self.nickel), "quarter: "+str(self.quarter), "bank balance: "+str(self.bank)]

bank = PiggyBank()
print("1. Show total in bank.")
print("2. Add a penny.")
print("3. Add a nickel.")
print("4. Add a dime.")
print("5. Add a quarter.")
print("6. Takeout money.")
print("Enter 0  to quit")
while True:
    choice = input("Enter your choice: ")
    if choice == "0":
        break
    elif (choice == "1"):
        display = bank.show_bank()
        print(display)
    elif (choice == "2"):
        num_pen = int(input("Number of pennies to be deposite: "))
        bank.add_penny(num_pen)
    elif (choice == "3"):
        num_nickel = int(input("Number of nickels to be deposite: "))
        bank.add_nickel(num_nickel)
    elif (choice == "4"):
        num_dime = int(input("Number of dimes to be deposite: "))
        bank.add_dime(num_dime)
    elif (choice == "5"):
        num_quarter = int(input("Number of quarters to be deposite: "))
        bank.add_quarter(num_quarter)
    elif (choice == "6"):
        withdraw = float(input("Enter the amount to withdraw: "))
        bank.take_out_money(withdraw)
    

    

