print("Enter the lenght of the ladder")
p = int(input())

if p < 3:
    print("NO, the monkey can't climb the pillar")
elif p % 2 == 1:
    print("YES, the monkey can climb the pillar")
else:
    print("NO, the monkey can't climb the pillar")
