print("Enter a date - Day Month Year")
x = input()
z = x.split()
d = z[0]
m = z[1]
y = z[2]

d = int(d)
m = int(m)
y = int(y)

month = [1, 3, 5, 7, 8, 10, 12]
day = 30
a = []

if m in month:
    day = 31
elif m == 2:
    day = 28
    if y % 4 == 0 and y % 100 != 0:
        day = 29
    elif y % 100 == 0 and y % 400 == 0:
        day = 29


if d == 0 or d > day:
    a = "Invalid Date"
elif m == 0 or m > 12:
    a = "Invalid Date"
else:
    pass

if d == day and m == 12:
    y = y + 1
    d = 1
    m = 1
elif d == day:
    m = m + 1
    d = 1
elif d < day:
    d = d + 1

if len(a) == 0:
    print("Next date:", d, m, y)
else:
    print(a)
