## DSA

numbers = [1, 2, 3, 4, 5]

k = int(input("Enter rotation position: "))

left = numbers[k:] + numbers[:k]

right = numbers[-k:] + numbers[:-k]

print("Left Rotation:", left)
print("Right Rotation:", right)