# Get the age of user
age = int(input("How old are you now?"))

years_to_90 = 90 - age

days_to_90 = years_to_90 * 365

weeks_to_90 = years_to_90 * 52

months_to_90 = years_to_90 * 12

print(f"You have {days_to_90} days, {weeks_to_90} weeks, and {months_to_90} months left.")