a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a <= 0 or b <= 0:
    print("Enter positive numbers")

else:
    smaller = a if a < b else b

    hcf = 1

    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            hcf = i

    lcm = a if a > b else b

    while lcm % a != 0 or lcm % b != 0:
        lcm += 1

    print("HCF:", hcf)
    print("LCM:", lcm)