# Professional Password Strength & Entropy Analyzer
This Python tool provides a high-level security analysis of user passwords. Unlike basic checkers, it uses mathematical entropy and security best practices to evaluate how "guessable" a password is for a computer.

## Features

* **Secure Input**: Uses ```getpass``` to hide passwords while typing, preventing "shoulder surfing."
* **Entropy Calculation**: Calculates the mathematical bits of security using *E = L \times \log_2(R)*.
* **Pattern Detection**: Identifies weak sequential patterns like "123" or "abc."
* **Specific Symbol Validation**: Checks against a professional set of allowed special characters.
* **Space Detection**: Flags accidental or insecure spaces within the password.
* **Error Handling**: Includes try-except blocks for a smooth, professional user experience.

## How It Works
1. Input: The script securely prompts for a password (text is invisible).
2. Analysis: It evaluates:
- **Numbers**: Does the password contain digits (e.g., 123)?
- **Lowercase** letters: Does the password include lowercase characters (e.g., a-z)?
- **Uppercase** letters: Does the password include uppercase characters (e.g., A-Z)?
- **Symbols**: Does the password include special characters (e.g., @, #, $)?
- **Length**: Is the password at least 8 characters long?
- **Character Pools**: Checks for Numbers, Lowercase, Uppercase, and Symbols.
- **Entropy**: Measures the "randomness" (50+ bits is generally considered professional-grade).
- **Logic Checks**: Scans for sequences and length (minimum 8 characters).
3. **Feedback**: Provides a detailed list of characteristics and actionable improvements.

## Requirements
- **Python 3.x**
- Standard libraries: ```math```, ```getpass```

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

```
Enter your password (it will be hidden): 

Your password has:
- Lowercase letters
- Uppercase letters
- Symbols
- Sufficient length (8 characters or more)
- Entropy Score: 56.42 bits

Your password is strong!
```

## Updates

* **Improved Feedback:** The script now provides more specific feedback about what criteria a password fails to meet (e.g., "Missing numbers," "Password too short"). This helps users create stronger passwords by giving them actionable information.
* **Modular Design**: The script is now wrapped in functions with a main entry point.
* **Mathematical Strength**: Added Entropy scoring to give a "Real-World" security metric.
* **Graceful Exits**: Added handling for KeyboardInterrupt (Ctrl+C).

## Upcoming Updates

*   **Common Password Check:**  Will check the password against a list of commonly used passwords or known breaches to prevent users from choosing easily guessable passwords.
*   **Symbol Definition:**  Will define a specific set of allowed symbols (e.g., punctuation marks, special characters) instead of flagging any non-alphanumeric character as a symbol. This will improve the accuracy of the symbol check.
*   **Character Type Combinations:** Will add a check for a minimum number of distinct character types present (e.g., at least 3 out of 4: numbers, lowercase, uppercase, symbols).  This encourages users to create passwords with a good mix of character types.
*   **Password History Check:** Will implement a check to see if the user has used the password before, preventing simple password rotation.
*   **Regular Expression Implementation:** Will explore using regular expressions to make the character checks more concise and readable.
*   **Context-Specific Testing**: We will add Optional Filters to test passwords specifically for different use cases (e.g., WiFi WPA2 passwords, Database credentials, or Personal Account security).

## Security Notes
- This script is for educational purposes only.
- Even though getpass is used, never type your actual banking passwords into any unencrypted script.

## License
This project is provided under the MIT License.