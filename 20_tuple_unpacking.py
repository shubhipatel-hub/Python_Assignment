numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

swapped = (last, *middle, first)

print("Original:", numbers)
print("After swapping:", swapped)