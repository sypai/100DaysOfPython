import random


def toss():
    random_int = random.randint(0, 1)

    if random_int == 1:
        print("Heads")
    else:
        print("Tails")

    return random_int


data = {"Heads": 0, "Tails": 0}

for _ in range(100):
    result = toss()
    if result == 1:
        data["Heads"] += 1
    else:
        data["Tails"] += 1

print(data)
