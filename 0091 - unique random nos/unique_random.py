
import random

unique = []

while True:
    number = random.randint(1,100)
    if number not in unique:
        unique.append(number)
    else:
        pass

    if len(unique) == 5:
        break

print("Random Unique nos. -", unique)
