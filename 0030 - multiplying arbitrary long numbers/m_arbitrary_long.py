print("Enter two numbers:")
x = input()
y  = input()
power = 10
n = 0
sum = 0
a = 0


for i in range(len(x)-1,-1,-1):
    n = 1
    if i < len(x) - 2:
        a = a + 1
    n = n + a

    for j in range(len(y)-1,-1,-1):
        if j == len(y)- 1 and i == len(x) - 1 :
            sum = sum + (int(x[i]) * int(y[j]))
        else:
            power = 10 ** n
            sum = sum + (int(x[i]) * int(y[j]) * power)
            n = n + 1

print("Product of the two numbers", sum)
