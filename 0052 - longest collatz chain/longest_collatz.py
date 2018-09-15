a = 1
b = 1
x = 0

while x < 1000000:
    x = x + 1
    y = x
    a = 1
    while y > 1:
        if y % 2 == 0:
            y = y/2
            a = a + 1
        else:
            y = 3*y + 1
            a = a + 1
    if a > b:
        b = a
        large_no = x

print("Starting number of longest collatz chain:", large_no)
print("Number of terms in the chain:", b)
