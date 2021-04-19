# Greet the customer
print("Thank you, for using the Tip Generator")

# Ask for the total bill amount in ₹
bill = float(input("What is the total bill amount (in ₹)?\n"))

# Ask for the number of people among which the bill has to be divided
divisor = float(input("How many people do you want to split the bill amongst?\n"))

# What percentage of the bill do you want to give as tip?
tip_cent = float(input("What percentage of the bill do you want to give as tip?\n"))
tip = (bill * tip_cent) / 100

# Print the amount that everyone has to pay
share = "{:.2f}".format((bill + tip) / divisor)

print("Each individual needs to pay, ₹ " + str(share))


