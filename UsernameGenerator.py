import random
import string

def generate_username(length=8):
    # Define the characters to choose from (you can adjust this if needed)
    characters = string.ascii_letters + string.digits  # Includes letters (both uppercase and lowercase) and digits

    # Generate a random username
    username = ''.join(random.choice(characters) for _ in range(length))
    return username

# Example usage:
if __name__ == "__main__":
    generated_username = generate_username()
    print(f"Generated username: {generated_username}")
