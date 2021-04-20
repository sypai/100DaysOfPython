def greet():
    print("================================================================="
          "\nWelcome!🙏 \nYou have reached the abode of the most loved pizzas in the world!")
    name = input("\nMay we know your name? \n")
    return name


def order(name):
    menu = "\n\t________________________________" + \
           "\n\t+ + + + Size   + + + + Price + +" + \
           "\n\t________________________________" + \
           "\n\t+ + 1)  Small  + + + +  $ 15 + +" + \
           "\n\t________________________________" + \
           "\n\t+ + 2)  Medium + + + +  $ 20 + +" + \
           "\n\t________________________________" + \
           "\n\t+ + 3)  Large  + + + +  $ 25 + +" + \
           "\n\t________________________________\n"

    print(f"\nHey, {name}! Here's our menu 📖 => {menu}")

    size_num = input("Tell us which one do you want? 1, 2 or 3 => ")
    if size_num is "1":
        size = "Small"
    elif size_num is "2":
        size = "Medium"
    else:
        size = "Large"

    add_pepperoni = input("\nDo you want us to add pepperoni to your pizza, Yes(y/Y) or No(n/N) => ")
    pepperoni = False
    if add_pepperoni is "Y" or add_pepperoni is "y":
        pepperoni = True
    pepperoni_status = "with" if pepperoni else "without"

    add_cheese = input("\nWould you like us to add extra cheese on your pizza"
                       ", Yes(y/Y) or No(n/N) => ")
    cheese = False
    if add_cheese is "Y" or add_cheese is "y":
        cheese = True
    cheese_status = "with" if cheese else "without"

    print(f"\nThank you, {name}! Let's confirm your order.\n\n"
          f"\tOne {size} pizza {pepperoni_status} "
          f"extra pepperoni and {cheese_status} extra cheese.\n")

    return size_num, pepperoni, cheese


name = greet()
while True:
    size, pepperoni, cheese = order(name)
    confirm = input("Press (Y/y) to CONFIRM | Press any other key to order again.")
    if confirm is "Y" or confirm is "y":
        pass
    else:
        continue

    print("\nGreat! We'll start preparing your pizza. Your patience is appreciated.\n")

    for _ in range(5):
        for wait in range(10099990):
            continue
        secs = 5 - _
        print(str(secs) + " secs...")

    print("\nHere! Your pizza is almost ready! ⏱. \n"
          "Please pay your Bill 💵 until then.")

    bill = 0
    if size is "1":
        bill += 15
        if pepperoni:
            bill += 2
    elif size is "2":
        bill += 20
        if pepperoni:
            bill += 3
    else:
        bill += 25
        if pepperoni:
            bill += 3

    if cheese:
        bill += 1

    show_bill = "\n\t_____________________________________" +\
                f"\n\t|      Total amount to pay: ${bill}     |" + \
                "\n\t-------------------------------------"
    print(show_bill)

    pay = input(f"\nPress P/p to pay ${bill}: ")

    if pay is 'P' or pay is 'p':
        pass
    else:
        print("Sorry, Your payment could not be processed. Try Ordering again!")
        continue

    print(f"\nThank you, {name}!. Let us bring your hot-n-delicious pizza to you\n")

    for _ in range(5):
        for wait in range(10099990):
            continue
        secs = 5 - _
        print(str(secs) + " secs...")

    print("\nHurray! Your pizza is here!")
    print("\n\t  🍕🍕🍕🍕🍕🍕\n\t    🍕🍕🍕🍕🍕\n\t      🍕🍕🍕🍕\n\t        🍕🍕🍕\n\t          🍕🍕\n\t            🍕")
    print(f"\nThank you for eating at Python Pizza! Have a great day!\nYou are the best, {name}!")
    print("=================================================================")
    break
