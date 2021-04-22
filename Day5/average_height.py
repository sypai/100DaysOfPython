height_input = input("Enter the heights of students (in cm) :")
heights = height_input.split()

count = 0
total = 0
for height in heights:
    total += int(height)
    count += 1

avg_height = round(total / count)

print(avg_height)