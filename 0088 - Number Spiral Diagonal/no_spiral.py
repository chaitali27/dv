n = 1
x = 0
z = 0
sum = 1

a = 1
b = 1
c = 1
d = 1

while z < 500:
    z = z + 1
    n = n + 2
    x = x + 1
    a = n**2
    sum = sum + a
    b = n**2 - 6*x
    sum = sum + b
    c = n**2 - 4*x
    sum = sum + c
    d = n**2 - 2*x
    sum = sum + d


print("Sum of the numbers on the diagonals in 1001 by 1001 spiral is",sum)
