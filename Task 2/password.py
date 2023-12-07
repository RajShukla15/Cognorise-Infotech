import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ""
    special_chars = string.punctuation if include_special_chars else ""

    # Combine character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Ensure the password length is at least 4 characters
    length = max(4, length)

    # Generate the password
    password = random.sample(all_chars, length)
    password = ''.join(password)

    return password

# Example usage:
password = generate_password()
print("Generated Password:", password)
