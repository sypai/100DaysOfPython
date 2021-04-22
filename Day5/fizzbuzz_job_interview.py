for _ in range(1, 101):
    if _ % 3 == 0 and _ % 5 == 0:
        print("FizzBuzz")
    elif _ % 3:
        print("Fizz")
    elif _ % 5 == 0:
        print("Buzz")
    else:
        print(_)
