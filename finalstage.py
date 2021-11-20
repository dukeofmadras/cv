
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
        if state == "SLIM BAR":
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
statex = input("Enter product you needed")
moneyx = int(input("Enter amount"))
checking = vendingMachine()
checking.operation(statex,moneyx)
remaning = change
z = print("Want to buy more items with remaining change ? (y/n)" )
if z == "y":
    a = input("Enter product name")
    checking1 = vendingMachine.operation(a,remaning)
else:
    print("Thank you")



