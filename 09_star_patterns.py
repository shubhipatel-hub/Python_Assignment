n = int(input("Enter number of rows: "))

# Triangle
print("Triangle")

for i in range(1, n + 1):
    print("* " * i)


# Pyramid
print("Pyramid")

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)


# Diamond
print("Diamond")

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * (2 * i - 1))