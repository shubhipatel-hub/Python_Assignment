sentence = input("Enter a sentence: ")

words = sentence.split()

if words:
    longest = max(words, key=len)

    print("Longest Word:", longest)
    print("Length:", len(longest))

else:
    print("No word found")