print("Hi! This is only place to get the most accurate BMI")

weight = float(input("Enter your weight (in Kilograms): "))
height = float(input("Enter your height (in centimetres): ")) / 100.0

BMI = weight / (height ** 2)

report = ""

if BMI <= 18.5:
    report = "you are underweight"
elif 18.5 < BMI <= 25:
    report = "you have a normal weight"
elif 25 < BMI <= 30:
    report = "you are slightly overweight"
elif 30 < BMI <= 35:
    report = "you are obese"
else:
    report = "you are clinically obese"

BMI = round(weight / (height ** 2))

print(f"Your BMI is {BMI}, {report}.")
