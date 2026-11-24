numbers = [1, 2, 3, 2, 4, 1, 5]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("Unique list:", result)