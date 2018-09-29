n = ''
nl = ''
pl = 0
p = 0
x = 1000
pal = 0
while pl == 0 and x > 500:
    x = x - 1
    for i in range(999,900,-1):
        p = x * int(i)
        p = str(p)
        for a in p:
            n = str(n) + a
            nl = a + str(nl)
        if n == nl:
            pl = int(p)
        else:
            pl = 0
        if pal < pl:
            pal = pl
        n = ''
        nl = ''




print("Largest palindrome number made from product of 2 three digit numbers:",pal)
