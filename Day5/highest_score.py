input_scores = input("Enter the scores of all the students: ")
scores = input_scores.split()

max_score = 0
for score in scores:
    if int(score) > max_score:
        max_score = int(score)

print(f"The highest score in the class is: {max_score}")
