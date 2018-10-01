x = []
t = 0

for i in range(2,101):
    for j in range(2,101):
        d = i ** j
        if d not in x:
            x.append(d)
            t = t + 1
y = len(x)
for i in range (0,y):
    for j in range (1,y-i):
        if(x[j-1]> x[j]):
            z = x[j-1]
            x[j-1] = x[j]
            x[j] = z


print("Sequence:")
print(x)
print("Number of terms generated:",t)
