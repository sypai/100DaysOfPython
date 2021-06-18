import math


def find_num_of_cans(height, width, cover):
    area = height * width
    cans = math.ceil(area / cover)
    print(f"You'll need {cans} cans of paint.")


find_num_of_cans(7, 13, 5)
