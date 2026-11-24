password = input("Enter password: ")

try:
    if len(password) < 8:
        raise Exception("Password length must be 8")

    if not any(ch.isupper() for ch in password):
        raise Exception("Add uppercase letter")

    if not any(ch.isdigit() for ch in password):
        raise Exception("Add a number")

    print("Valid Password")

except Exception as e:
    print("Error:", e)