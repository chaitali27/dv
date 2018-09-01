print("Enter two Fractions: ")

a = input("Numerator1: ")
b = input("Denominator1: ")
c = input("Numerator2: ")
d = input("Denominator2: ")

if int(b) == 0 or int(d) == 0:
    print("Fraction is not defined so it cannot be added")
elif int(b) == int(d):
    n = int(a) + int(c)
    d = int(b)
    if n % d == 0:
        print("Sum of both the Fractions is",n//d)
    else:
        print("Sum of both the Fractions is",n,"/",d)


else:
    x = int(a)*int(d) + int(c)*int(b)
    y = int(b)*int(d)
    if x % y == 0:
        print("Sum of both the Fractions is",x//y)
    else:
        print("Sum of both the Fractions is",x,"/",y)
