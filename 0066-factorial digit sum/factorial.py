n = 100
y = 1

while(n>0):
    y = y * n
    n = n - 1

y = str(y)
x = 0
for i in y:
    x = x + int(i)
print (x)
