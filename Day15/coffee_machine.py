import datetime

items = {
    'water': 500,
    'milk': 500,
    'coffee': 50
}

requirements = { # water, milk, coffee
    'espresso': [50, 0, 18],
    'latte': [200, 150, 24],
    'cappuccino': [250, 100, 24],
}
## Let's not use cash-box or different coins, as returning change will have to 
## be another calcution
# cash_box = {
#     '1': 5,  # Penny
#     '5': 5,  # Nickles
#     '10': 2, # Dimes
#     '25': 1  # Quarters
# }

money = 250 #cents

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

def check_items(requirements, coffee, items):
    items_flag = [0, 0, 0]
    if items.get('water') >= requirements.get(coffee)[0]:
        items_flag[0] = 1
    else:
        print("Sorry there's not enough Water.")

    if items.get('milk') >= requirements.get(coffee)[1]:
        items_flag[1] = 1
    else:
        print("Sorry there's not enough Milk.")
    
    if items.get('coffee') >= requirements.get(coffee)[2]:
        items_flag[2] = 1
    else:
        print("Sorry there's not enough coffee.")

    if items_flag[0] == 1 and items_flag[1] == 1 and items_flag[2] == 1:
        print(f"\nJust a moment! I am getting your {coffee} ready.")
        items['water'] -= requirements.get(coffee)[0]
        items['milk'] -= requirements.get(coffee)[1]
        items['coffee'] -= requirements.get(coffee)[2]
        return True, items 
    else:
        return False, items   

def payment(price, money):
    money_in = 0
    success = False
    
    while not success: 
        print("\nPlease insert coins ===> ")
        quarters = int(input("How many Quarters? "))
        dimes = int(input("How many Dimes? "))
        nickels = int(input("How many Nickels? "))
        penny = int(input("How many Pennies? "))
        money_in += (quarters * 25) + (nickels * 5) + (dimes * 10) + (penny)
            
        if money_in < price:
            diff = price - money_in
            print(f"You need to pay {diff} more cents!")

        elif money_in > price:
            diff = price - money_in
            print(f"Here's your change. Please collect {-diff} cents!")
            money_in = price
            success = True
        
        else:
            success = True

    return money_in + money

def coffee(requirements, items, money):
    print("\n-------------------------")
    print("1. Espresso - $ 1.50")
    print("2. Latte - $ 2.50")
    print("3. Cappuccino - $ 3.00")
    print("-------------------------\n")
    choice = input("What would you like to drink?  1/2/3 ==> ")
    
    if choice == '1':
        is_available, items = check_items(requirements, 'espresso', items)
        if is_available:
            money = payment(150, money)
            print("\nHere's your espresso buddy! Enjoy.")
            
    
    elif choice == '2':
        is_available, items = check_items(requirements, 'latte', items)
        if is_available:
            money = payment(250, money)
            print("\nHere's your latte buddy! Enjoy.")
            

    elif choice == '3':
        is_available, items = check_items(requirements, 'cappuccino', items)
        if is_available:
            money = payment(300, money)
            print("\nHere's your cappuccino buddy! Enjoy.")
    return money

def report(items, money):
    water = items.get('water')
    milk = items.get('milk')
    coffee = items.get('coffee')
    money_dollar = money / 100
    print(f"\n\nI currently have $ {money_dollar} inside me.\n")
    print(f"Here's all that I have: \n\n\t | WATER | {water} ml |\n\t | MILK  | {milk} ml |\n\t |COFFEE | {coffee} gm |")

def open(items, money):
    water = int(input("How much Water are you adding? (in ml): "))
    milk = int(input("How much milk are you adding? (in ml): "))
    coffee = int(input("How much coffee are you adding? (in gm): "))
    items['water'] += water
    items['milk'] += milk
    items['coffee'] += coffee
    return items

while True:
    greet()
    response = input("\nWhat would you like?  ")
    if response == 'coffee':
        money = coffee(requirements, items, money)

    elif response == 'report':
        report(items, money)
    
    elif response == 'open':
        items = open(items, money)
        print("Thank you for filling me up!")
        report(items, money)

    elif response == 'off':
        print("\nBeep.\nBoop.\nBeep.\nI am going to sleep.")
        break

    print("\n==============================================================\n")