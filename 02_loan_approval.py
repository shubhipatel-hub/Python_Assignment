salary = float(input("Enter salary: "))
credit_score = int(input("Enter credit score: "))
age = int(input("Enter age: "))

if salary >= 30000 and credit_score >= 700 and 21 <= age <= 60:
    print("Loan Approved")

elif sum([
    salary >= 30000,
    credit_score >= 700,
    21 <= age <= 60
]) == 2:
    print("Conditionally Approved")

else:
    print("Loan Rejected")