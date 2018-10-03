n = 1
y = 0
z = 0

while y < 10001:
    n = n + 1
    p = n//2 + 1
    for i in range(2,p):
        if n % i == 0:
            break
    else:
        y = y + 1
        z = n

print("10001th prime number is ",z)
