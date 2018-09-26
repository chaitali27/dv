print("Enter a Number")
a = input()
a = int(a)
k = 0
y = -1
x = []

def factorial(b):
    fac = 1
    for i in range(1,b + 1):
        fac = fac * i
    return int(fac)

def coeff(b,c):
    co = factorial(b)/(factorial(b-c)*factorial(c))
    return int(co)


for i in range(0,a + 1):
    k = 0
    y = y + 1
    for j in range(y + 1):
        print(coeff(y,k),"  ",  end = "")
        k = k + 1
    print(end = "\n")
