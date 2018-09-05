x = [5, 1, 4, 2, 8]
print("list", x, end ='\n')
print(end = '\n')
y = len(x)

for i in range (0,y):
    for j in range (1,y-i):
        if(x[j-1]> x[j]):
            z = x[j-1]
            x[j-1] = x[j]
            x[j] = z
            print("Pass", i +1, x)
print(end = '\n')
print("sorted list", x)
