import re


def check_password_strength(password):
    # Initialize strength variables
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[\W_]', password))
    common_patterns = ['123', 'abc', 'password', 'qwerty', '111']

    # Evaluate the password
    score = 0
    suggestions = []

    # Length check
    if length >= 8:
        score += 1
    else:
        suggestions.append('Password should be at least 8 characters long.')

    # Complexity check
    if has_upper:
        score += 1
    else:
        suggestions.append('Password should include at least one uppercase letter.')

    if has_lower:
        score += 1
    else:
        suggestions.append('Password should include at least one lowercase letter.')

    if has_digit:
        score += 1
    else:
        suggestions.append('Password should include at least one digit.')

    if has_special:
        score += 1
    else:
        suggestions.append('Password should include at least one special character.')

    # Uniqueness check
    if not any(pattern in password for pattern in common_patterns):
        score += 1
    else:
        suggestions.append('Password contains common patterns or sequences.')

    # Determine strength
    if score == 5:
        strength = 'Very Strong'
    elif score == 4:
        strength = 'Strong'
    elif score == 3:
        strength = 'Moderate'
    else:
        strength = 'Weak'

    return strength, suggestions


def get_password_from_user():
    while True:
        password = input("Enter your password: ")
        strength, suggestions = check_password_strength(password)

        print(f'Password Strength: {strength}')
        if strength == 'Very Strong' or strength == 'Strong':
            print("Your password is strong enough.")
            break
        else:
            print("Suggestions to improve your password:")
            for suggestion in suggestions:
                print(f'- {suggestion}')


if __name__ == "__main__":
    get_password_from_user()