import random
import string

def generate_random_string(length=5):
    # Define the characters you want in the string (letters, digits, etc.)
    characters = string.ascii_letters + string.digits  # Includes a-z, A-Z, and 0-9
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# # Example usage:
# random_str = generate_random_string(10)
# print(f"Random String: {random_str}")
