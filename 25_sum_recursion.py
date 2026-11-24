def natural_sum(n):

    if n == 0:
        return 0

    return n + natural_sum(n - 1)


num = int(input("Enter number: "))

print("Sum:", natural_sum(num))