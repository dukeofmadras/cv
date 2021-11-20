#defining constant values
import sys
FIVE = "SLIM BAR"
TEN = "FAR BAR"
TWENTY = "MAR BAR"
FIFTY = "TWIN BAR"

class vendingMachine():
    def __init__(self, state, money):
        self.money = 0
        super().__init__()
        self.state = state

    def operation(self, state, money):
        if state in ["SLIM BAR" , "slim bar", "slimbar", "SLIMBAR" ]:
            print("Slim Bar Selected")
            if money >= 5:
                print("Here's your Slim bar")
                change = money - 5
                print("Take your change", change)
            else:
                print("Insufficient cash")
            return change

        elif state == "FAR BAR":
            print("Far Bar Selected")
            if money >= 10:
                print("Here's your Slim bar")
                change = money - 10
                print("Take your change", change)
            else:
                print("Insufficient cash")
            return change

        elif state == "MAR BAR":
            print("Mar Bar selected")
            if money >= 20:
                print("Here's your Slim bar")
                change = money - 20
                print("Take your change", change)
            else:
                print("Insufficient cash")
            return change

        elif state == "TWIN BAR":
            print("Twin Bar selected")
            if money == 50:
                print("Here's your Slim bar")
                change = money - 50
                print("Take your change", change)
            else:
                print("Insufficient cash")
            return change
        else: print("Invalid response")





print('Welcome to the vending machine!')
print("Welcome!, Please select any product you want. Slim bar, Far bar, Mur bar and Twin bar")
print("Slim bar - 5p, Far bar - 10p, Mur bar- 20p and Twin bar - 50p")
statex = str(input("Enter product you needed"))
moneyx = int(input("Enter amount"))
checking = vendingMachine(statex, moneyx)
change = checking.operation(statex,moneyx)
remaning = change
z = input("Want to buy more items with remaining change ? (y/n)" )
if z in ["y", "yes", "Y", "YES"]:
    a = input("Enter product name")
    checking1 = checking.operation(a,remaning)
else:
    print("Thank you")
