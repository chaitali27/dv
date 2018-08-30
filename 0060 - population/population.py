A = 50000000
B = 70000000
y = 0
while(A < B):

    A = A + (A*3/100)
    B = B + (B*2/100)
    y = y + 1

print("Number of years required for A to surpass B are", y)
