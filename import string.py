import string
import secrets

def generate_password(length=12):
    """
    Generate a secure random password.
    
    :param length: Length of the password (minimum 4 for complexity)
    :return: Randomly generated password string
    """
    if not isinstance(length, int) or length < 4:
        raise ValueError("Password length must be an integer >= 4")

    # Define character sets
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # Special characters

    # Ensure password has at least one of each type
    password_chars = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(symbols),
        secrets.choice(letters.upper())
    ]

    # Fill the rest of the password length with random choices
    all_chars = letters + digits + symbols
    password_chars += [secrets.choice(all_chars) for _ in range(length - 4)]

    # Shuffle to avoid predictable patterns
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)

if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length (min 4): "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
