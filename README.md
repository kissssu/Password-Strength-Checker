# Password Strength Checker
This Python script evaluates the strength of a user-provided password based on various criteria. It checks for:
- The presence of **numbers, lowercase letters, uppercase letters** and **symbols**.
- A **minimum length of 8 characters**.

## Features

*   Checks for the presence of numbers, lowercase letters, uppercase letters, and symbols.
*   Verifies if the password meets the minimum length requirement (8 characters).
*   Provides a summary of the password's characteristics (e.g., presence of numbers, letters, etc.).
*   Gives overall feedback on password strength.
*   Identifies missing components in your password.
*   User-friendly and easy-to-use.

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
```
git clone https://github.com/kissssu/Password-Strength-Checker.git
cd Password-Strength-Checker
```
2. Run the script using Python:
```bash
python3 password_checker.py
```

## Sample Output
#### Input:

```
Hello Ji.
Enter your password: Enter_your_password_herr.

Your password has:
- Lowercase letters
- Uppercase letters
- Symbols
- Sufficient length (8 characters or more)

Your password could be stronger. It needs:
- Missing numbers
```

## Updates

*   **Improved Feedback:** The script now provides more specific feedback about what criteria a password fails to meet (e.g., "Missing numbers," "Password too short"). This helps users create stronger passwords by giving them actionable information.

## Upcoming Updates

*   **Common Password Check:**  Will check the password against a list of commonly used passwords or known breaches to prevent users from choosing easily guessable passwords.
*   **Symbol Definition:**  Will define a specific set of allowed symbols (e.g., punctuation marks, special characters) instead of flagging any non-alphanumeric character as a symbol. This will improve the accuracy of the symbol check.
*   **Character Type Combinations:** Will add a check for a minimum number of distinct character types present (e.g., at least 3 out of 4: numbers, lowercase, uppercase, symbols).  This encourages users to create passwords with a good mix of character types.
*   **Password History Check:** Will implement a check to see if the user has used the password before, preventing simple password rotation.
*   **Regular Expression Implementation:** Will explore using regular expressions to make the character checks more concise and readable.

## Security Notes
- This script is for educational purposes only.
- Do **NOT** use it to process sensitive or actual user passwords.
- Always secure sensitive password-handling tools using encryption and secure storage.

## License
This project is provided under the MIT License.