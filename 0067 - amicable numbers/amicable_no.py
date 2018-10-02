x = 0
sum = 0
sum1 = 0
sum2 = 0
s2 = []

print("Amicable Pairs:")
while x < 10000:
    x = x + 1
    sum = 0
    sum1 = 0
    s = []
    s1 = []
    for i in range(1,x):
        if x % i == 0:
            sum = sum + int(i)

    for j in range(1,sum):
        if sum % j == 0:
            sum1 = sum1 + int(j)

    if x  == sum1 and x != sum and x not in s2:
        sum2 = sum2 + x + sum
        print(x,sum)
        s2.append(x)
        s2.append(sum)

print("Sum of Amicable Pairs:",sum2)
