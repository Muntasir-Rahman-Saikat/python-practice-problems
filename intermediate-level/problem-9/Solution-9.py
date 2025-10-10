# password_validator.py

import re

def validate_password(password):
    errors = []

    # Minimum length check
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    # Uppercase check
    if not any(c.isupper() for c in password):
        errors.append("Password must contain at least one uppercase letter.")

    # Lowercase check
    if not any(c.islower() for c in password):
        errors.append("Password must contain at least one lowercase letter.")

    # Number check
    if not any(c.isdigit() for c in password):
        errors.append("Password must contain at least one number.")

    # Special character check (regex: anything not letter or digit)
    if not re.search(r"[^A-Za-z0-9]", password):
        errors.append("Password must contain at least one special character.")

    # Final result
    if errors:
        print("❌ Invalid password:")
        for e in errors:
            print(" -", e)
    else:
        print("Password is valid!")


if __name__ == "__main__":
    user_input = input("Enter your password: ")
    validate_password(user_input)
