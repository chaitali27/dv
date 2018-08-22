def reverse_sum_and_check_equality(x):
    sum = 0
    reverse_sum = 0
    for i in x:
        sum = int(sum) + int(i)
        reverse_sum = int(i) + int(reverse_sum)

    if sum == reverse_sum:
        print (True)
        return True
    else:
        print (False)
        return False

a = input("enter a number: ")
reverse_sum_and_check_equality(a)
