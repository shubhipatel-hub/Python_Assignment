age = int(input("Enter age: "))

try:
    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("Valid age")

except ValueError as e:
    print("Error:", e)