balance = 5000

amount = int(input("Enter withdrawal amount: "))

try:
    if amount > balance:
        raise Exception("Insufficient Balance")

    balance -= amount

    print("Withdrawal successful")
    print("Remaining balance:", balance)

except Exception as e:
    print("Error:", e)