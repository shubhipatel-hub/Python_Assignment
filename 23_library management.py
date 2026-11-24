library = {
    "Python": 5,
    "Java": 3,
    "SQL": 4
}

book = input("Enter book name: ")

if book in library:
    print("Available quantity:", library[book])

    issue = int(input("Enter quantity to issue: "))

    if issue <= library[book] and issue > 0:
        library[book] -= issue
        print("Book issued successfully")
    else:
        print("Not enough books available")

else:
    print("Book not found")

print("Updated Library:", library)