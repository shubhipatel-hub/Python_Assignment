students = {
    "Aman": 80,
    "Riya": 90,
    "Rahul": 25,
    "Neha": 70
}

topper = max(students, key=students.get)

average = sum(students.values()) / len(students)

failures = []

for name, marks in students.items():
    if marks < 33:
        failures.append(name)

print("Topper:", topper)
print("Average:", average)
print("Failed students:", failures)