def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string 
if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

# Get input from the user
user_input = input("Enter a string to check if it's a palindrome: ")


if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")