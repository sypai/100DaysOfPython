print("Hi! This is only place to get the most accurate BMI")

weight = float(input("Enter your weight (in Kilograms): "))
height = float(input("Enter your height (in centimetres): ")) / 100.0

BMI = weight // (height ** 2)

print("Your Body Mass Index(BMI) is: " + str(BMI) + " kg / m^2")
