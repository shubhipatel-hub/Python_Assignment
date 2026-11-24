from datetime import datetime, date

now = datetime.now()

print("Current Date and Time:", now)

dob = input("Enter DOB (DD-MM-YYYY): ")

birth = datetime.strptime(dob, "%d-%m-%Y").date()

today = date.today()

age = today.year - birth.year

if (today.month, today.day) < (birth.month, birth.day):
    age -= 1

print("Your Age:", age)