text = input("Enter a string: ")

cleaned = text.lower().replace(" ", "")

if cleaned == cleaned[::-1]:
    print("Palindrome String")

else:
    print("Not a Palindrome String")