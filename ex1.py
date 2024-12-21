
word = input("Enter a word: ").strip().lower()

# Checks if the string is a palindrome
if word == word[::-1]:
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')