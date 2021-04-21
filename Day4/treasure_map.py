import random

row1 = ["__", "__", "__"]
row2 = ["__", "__", "__"]
row3 = ["__", "__", "__"]

print("Welcome to Treasure Hunt. Here's our treasure map:\n")
print(f"\t{row1}\n\t{row2}\n\t{row3}")

row = random.randint(0, 2)
column = random.randint(0, 2)
if row == 0:
    row1[column] = "🥇"
elif row == 1:
    row2[column] = "🥇"
else:
    row3[column] = "🥇"

print("\nWhere do you think the treasure is?\n")
in_row = int(input("Enter Row => ")) - 1
in_column = int(input("Enter Column => ")) - 1


if row == in_row and column == in_column:
    print("\nYou are absolutely correct, You win!")
    print(f"\t{row1}\n\t{row2}\n\t{row3}")

else:
    print("\nYou chose X location, but the treasure wasn't there! You lose!")
    if in_row == 0:
        row1[in_column] = " X"
    elif in_row == 1:
        row2[in_column] = " X"
    else:
        row3[in_column] = " X"
    print(f"\t{row1}\n\t{row2}\n\t{row3}")



