#!/usr/bin/python3
import getpass
import math

def check_password_strength():
    try:
        password = getpass.getpass("Enter your password (it will be hidden): ")
        
        if not password:
            print("Error: Password cannot be empty.")
            return

        special_chars = "!@#$%^&*()-_=+[]{};:,.<>?/"
        
        # Flags
        has_number = False
        has_lowercase = False
        has_uppercase = False
        has_symbol = False
        has_space = False
        has_sequential = False

        # 1. Calculate Character Pool Range (R) for Entropy
        pool_size = 0
        if any(c.isdigit() for c in password): 
            has_number = True
            pool_size += 10
        if any(c.islower() for c in password): 
            has_lowercase = True
            pool_size += 26
        if any(c.isupper() for c in password): 
            has_uppercase = True
            pool_size += 26
        if any(c in special_chars for c in password): 
            has_symbol = True
            pool_size += len(special_chars)
        if any(c.isspace() for c in password):
            has_space = True
            pool_size += 1

        # 2. Sequential check
        for i in range(len(password) - 2):
            part = password[i:i+3].lower()
            if part in "abcdefghijklmnopqrstuvwxyz" or part in "0123456789":
                has_sequential = True

        # 3. Real-World Entropy Calculation
        # Formula: bits = length * log2(pool_size)
        length = len(password)
        length_ok = length >= 8
        entropy = 0
        if pool_size > 0:
            entropy = length * math.log2(pool_size)

        # --- Output Section (Format Unchanged) ---
        print("\nYour password has:")
        if has_number: print("- Numbers")
        if has_lowercase: print("- Lowercase letters")
        if has_uppercase: print("- Uppercase letters")
        if has_symbol: print("- Symbols")
        
        if length_ok:
            print("- Sufficient length (8 characters or more)")
        else:
            print("- Insufficient length (less than 8 characters)")

        # Professional Metric Tweak
        print(f"- Entropy Score: {entropy:.2f} bits")

        # Feedback
        feedback = []
        if not has_number: feedback.append("- Missing numbers")
        if not has_lowercase: feedback.append("- Missing lowercase letters")
        if not has_uppercase: feedback.append("- Missing uppercase letters")
        if not has_symbol: feedback.append("- Missing symbols")
        if not length_ok: feedback.append("- Insufficient length (less than 8 characters)")
        if has_space: feedback.append("- Contains spaces (not recommended)")
        if has_sequential: feedback.append("- Contains easy patterns like '123' or 'abc'")
        
        # Real-life tip: 50+ bits is usually considered "good"
        if entropy < 40 and not feedback:
            feedback.append("- Low randomness (entropy). Try making it longer.")

        if feedback:
            print("\nYour password could be stronger.")
            for message in feedback:
                print(message)
        else:
            print("\nYour password is strong!")

    except KeyboardInterrupt:
        print("\n\nProgram closed by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    check_password_strength()