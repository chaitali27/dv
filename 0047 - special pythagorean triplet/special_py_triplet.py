for x in range(1,1000):
    for y in range(x,1000):
        for z in range(y,1000):
            if x + y + z == 1000 and z*z == x*x + y*y:
                print("Triplets -", x, y, z, "and their Product-", x*y*z)
