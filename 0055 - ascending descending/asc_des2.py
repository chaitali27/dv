x = []
print("Enter five Numbers")

for i in range(5):
    y = int(input())
    x.append(y)
print(x)

if x[0] < x[1] < x[2] < x[3] < x[4]:
    print("Ascending")
elif x[0] > x[1] > x[2] > x[3] > x[4]:
    print("Descending")
else:
    print("None")
