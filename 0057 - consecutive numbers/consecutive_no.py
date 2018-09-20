
x = int(input("Enter a number: "))
y = 0

for i in range(x):
    for j in range (i + 1):
        y = y + 1
        print(y, end = " ")

    print(" ")
