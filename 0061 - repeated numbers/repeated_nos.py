x = [0, 1, 0, 13, 0, 5, 7, 8, 8, 0]
print("Number sequence:", x)

y = []

for i in range(0,10):
    for j in range(i + 1,10):
        if x[i] == x[j]:
            z = x[i]
            if z not in y:
                y.append(z)

print("Repeated numbers:", y)
