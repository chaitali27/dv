x = 1
y = 1
z = 2
index = 3

while len(str(z)) <= 999:

    x = y
    y = z
    z = x + y
    index = index + 1

print(end = "\n")
print("Index of the first term in the Fibonacci sequence to contain thousand digits - ", index, end = "\n")
print(end = "\n")
print("Thousand digit number: ", end = "\n")
print(z)
