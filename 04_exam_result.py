marks = []

for i in range(1, 6):
    m = int(input(f"Enter marks of subject {i}: "))
    marks.append(m)

if any(m < 33 for m in marks):
    print("Result: Fail")

else:
    percentage = sum(marks) / 5

    print("Percentage:", percentage)

    if percentage >= 60:
        print("First Division")

    elif percentage >= 50:
        print("Second Division")

    elif percentage >= 40:
        print("Third Division")

    else:
        print("Division not specified")