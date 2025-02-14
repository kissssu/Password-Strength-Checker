#!/usr/bin/python3

print("Hello Ji.")
password = input("Enter your password: ")

# Initialize flags
has_number = False
has_lowercase = False
has_uppercase = False
has_symbol = False

# Check password length
length_ok = len(password) >= 8

# Iterate through the password to check conditions
for i in password:
    if i.isdigit():
        has_number = True
    elif i.islower():
        has_lowercase = True
    elif i.isupper():
        has_uppercase = True
    else:
        has_symbol = True

# Print results
print("\nYour password has:")
if has_number:
    print("- Numbers")
if has_lowercase:
    print("- Lowercase letters")
if has_uppercase:
    print("- Uppercase letters")
if has_symbol:
    print("- Symbols")
if length_ok:
    print("- Sufficient length (8 characters or more)")
else:
    print("- Insufficient length (less than 8 characters)")

# Check overall password strength
if all([has_number, has_lowercase, has_uppercase, has_symbol, length_ok]):
    print("\nYour password is strong!")
else:
    print("\nYour password could be stronger. Consider including all character types and ensuring a length of at least 8 characters.")
