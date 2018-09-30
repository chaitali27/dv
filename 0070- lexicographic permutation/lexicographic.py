#please refer to the images first

p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 1000000
b = a - 1
c = 1
d = 0
n = 0
y = 0
z = 0
x = []
fac = ''
num = ''

print("Digits: ",p)

# converting the 999999 into factorial system number
while c > 0:
    n = n + 1
    c = b // n
    d = b % n
    x.append(d)
    b = c

for i in x:
    fac = str(i) + fac

print("Factorial Number: ",fac)

# converting factorial system number into millionth term
for i in range(10):
    y = int(fac[i])
    z = int(p[y])
    p.pop(y)
    num = num + str(z)


print("Millionth lexicographic permutation: ",num)
