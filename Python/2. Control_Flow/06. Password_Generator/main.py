import string
import random

# Character pools
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Combine all characters
character_pool = uppercase_letters + lowercase_letters + digits + special_characters

# Ask user for password length
while True:
    try:
        length = int(input("Enter desired password length (minimum 6): "))
        if length < 6:
            print("Please enter a length of at least 6.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Generate password
password = "".join(random.choice(character_pool) for _ in range(length))

print(f"Generated password: {password}")
