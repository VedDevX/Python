# Palindrome Checker Function

def is_palindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    
    return cleaned == cleaned[::-1]

user_input = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_input):
    print("Yes! It's a Palindrome.")
else:
    print("No! It's not a Palindrome.")