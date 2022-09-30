import datetime
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def greet():
    greetStr = "Good day!"
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        greetStr = "Good Morning!"
    elif 12 <= currentTime.hour <= 17:
        greetStr = "Good Afternoon!"
    else:
        greetStr = "Good Evening!"

    print(f"{greetStr} I am Coco, your coffee-machine!")
    print("\n== To order from my coffee menu, type 'coffee'\n== To check what's inside me, type 'report'\n== To fill me up, type 'Open'\n== To switch me off, type 'off'")


while True:
    # Greeting the user 
    greet()

    # Creating objects
    menu = Menu()
    # menuItem = MenuItem()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    # Taking User input
    response = input("\nWhat would you like?  ")

    # If user chooses coffee
    # Show available drinks, take input
    # Check if resources are sufficient for the chosen drink
    # If yes, make coffee, take money by checking cost return change

    if response == 'coffee':
        items = menu.get_items()
        order = input(f'\n What would you like to drink? {items} => ')

        drink = menu.find_drink(order)
    
        # name = menu_item.name
        # cost = menu_item.cost
        # ingredients = menu_item.ingredients
        # print(name, cost, ingredients)
        
        if coffee_maker.is_resource_sufficient(drink):
            print(f"You need to pay ${drink.cost}")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


    elif response == 'report':
        coffee_maker.report()
        money_machine.report()

    # elif response == 'open':
    #     items = open(items, money)
    #     print("Thank you for filling me up!")
    #     report(items, money)

    elif response == 'off':
        print("\nBeep.\nBoop.\nBeep.\nI am going to sleep.")
        break

    print("\n==============================================================\n")