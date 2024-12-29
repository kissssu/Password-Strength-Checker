# Password Strength Checker
This Python script evaluates the strength of a user-provided password based on various criteria. It checks for:
- The presence of **numbers, lowercase letters, uppercase letters** and **symbols**.
- A **minimum length of 8 characters**.

## Features
- Identifies missing components in your password.
- Provides feedback to help improve password strength.
- User-friendly and easy-to-use.

## How It Works
1. The script prompts the user to enter a password.
2. It checks the following:
- **Numbers**: Does the password contain digits (e.g., 123)?
- **Lowercase** letters: Does the password include lowercase characters (e.g., a-z)?
- **Uppercase** letters: Does the password include uppercase characters (e.g., A-Z)?
- **Symbols**: Does the password include special characters (e.g., @, #, $)?
- **Length**: Is the password at least 8 characters long?
3. It provides detailed feedback and evaluates if the password is strong.

## Requirements
- **Python 3.x**

## Usage
1. Clone or download this script.
2. Run the script using Python:
```bash
python3 password_checker.py
```
3. Enter your password when prompted.

## Example

#### Input:
```
Enter your password: Hello123
```

#### Output:
```
Hello Ji.

Your password has:
- Numbers
- Lowercase letters
- Uppercase letters
- Insufficient length (less than 8 characters)

Your password could be stronger. Consider including all character types and ensuring a length of at least 8 characters.
```

## Security Notes
- This script is for educational purposes only.
- Do **NOT** use it to process sensitive or actual user passwords.
- Always secure sensitive password-handling tools using encryption and secure storage.

## License
This project is provided under the MIT License.

