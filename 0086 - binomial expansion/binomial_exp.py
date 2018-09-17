print("Enter a power")
a = input()
a = int(a)
k = 1
x = []

def factorial(b):
    fac = 1
    for i in range(1,b + 1):
        fac = fac * i
    return int(fac)

def coeff(b,c):
    co = factorial(b)/(factorial(b-c)*factorial(c))
    return int(co)

coeff(a,k)

print("(x + y)^", end = "")
print(a,"= ", end = "")
print(" x^", end = "")
print(a, " +  ", end = "")


for i in range(1,a):
    print(coeff(a,k),"*", end = "")
    print("x^", end = "")
    print(a-k,"*", end = "")
    print("y^", end = "")
    print(k, " +  ", end = "")
    k = k + 1


print(" y^",end = "")
print(a)
