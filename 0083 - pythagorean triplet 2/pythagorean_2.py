print("Enter three numbers")
x = input()
y = input()
z = input()

if int(x)*int(x) == int(y)*int(y) + int(z)*int(z) or int(z)*int(z) == int(y)*int(y) + int(x)*int(x) or int(y)*int(y) == int(x)*int(x) + int(z)*int(z):
    print("True, the numbers are Pythagorean Triplets")
else:
    print("False, the numbers are not Pythagorean Triplets")
