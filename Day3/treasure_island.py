print(r'''
        | |                                    
        | |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
        | __| '__/ _ \/ _` / __| | | | '__/ _ \
        | |_| | |  __/ (_| \__ \ |_| | | |  __/
         \__|_|  \___|\__,_|___/\__,_|_|  \___|
         
                    (_)   | |               | |
                     _ ___| | __ _ _ __   __| |
                    | / __| |/ _` | '_ \ / _` |
                    | \__ \ | (_| | | | | (_| |
                    |_|___/_|\__,_|_| |_|\__,_|
                                               

    ''')

print("\nWelcome to Treasure Island. Your mission is to find the treasure.")

print("======================================================================\n")

print("You are on a cross-road! Which road to choose?\nLEFT (⬅) OR RIGHT(➡)")
choice = input("\nPress L/l for left | Press R/r for right ===> ")

if choice == 'R' or choice == 'r':
    print("You have fallen into hole. GAME ENDS!")
    exit(0)

else:
    print("======================================================================\n")

    print("You have reached the bank of a river.\nYou can either start swimming (🏊) or "
          "wait here for a boat (🚣).")
    choice = input("\nPress S/s for swimming | Press W/w for waiting ===> ")

    if choice == 'S' or choice == 's':
        print("You got eaten by a crocodile! Your quest ends here. You lose!")

    else:
        print("======================================================================\n")

        print("Nice that you waited. You have been brought to the other side of the"
              " river and now you have three doors(🚪) in front of you. \n"
              "A 🟨 Yellow door, a 🟥 Red Door and a 🟦 Blue Door. Which one do you want to open."
              " You will be pushed inside.\n")
        choice = input("Press Y/y for Yellow | Press R/r for red | Press B/b for Blue")

        if choice == 'R' or choice == 'r':
            print("You burnt in fire🔥! You lose!")

        elif choice == 'B' or choice == 'b':
            print("You were thrown from clouds into sky ☁! You'll die eventually! You lose!")

        elif choice == 'Y' or choice == 'y':
            print("Yay! You win! You got the treasure.🥇")
            print(r'''
                    
                                _.--.
                            _.-'_:-'||
                        _.-'_.-::::'||
                   _.-:'_.-::::::'  ||
                 .'`-.-:::::::'     ||
                /.'`;|:::::::'      ||_
               ||   ||::::::'     _.;._'-._
               ||   ||:::::'  _.-!oo @.!-._'-.
               \'.  ||:::::.-!()oo @!()@.-'_.|
                '.'-;|:.-'.&$@.& ()$%-'o.'\U||
                  `>'-.!@%()@'@_%-'_.-o _.|'||
                   ||-._'-.@.-'_.-' _.-o  |'||
                   ||=[ '-._.-\U/.-'    o |'||
                   || '-.]=|| |'|      o  |'||
                   ||      || |'|        _| ';
                   ||      || |'|    _.-'_.-'
                   |'-._   || |'|_.-'_.-'
                    '-._'-.|| |' `_.-'
                        '-.||_/.-'

                ''')

print("======================================================================\n")
