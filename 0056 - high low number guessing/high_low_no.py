import random

m = int(input("Enter the uppermost number: "))
x = random.randint(1, m)
y = 0

while True:
    print("Guess the number!")
    z = int(input())
    if (z < x):
        print("Low")
        y = y + 1
    elif (z > x):
        print("High")
        y = y + 1
    elif z == x :
        print("Correct")
        y = y + 1
        break

print("Attempts taken to correctly guess the number:", y)
