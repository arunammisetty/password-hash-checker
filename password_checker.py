import hashlib
import re

# Function to hash the password using SHA-256
def hash_password(password):
    # Hash the password with SHA-256
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed

# Function to check password strength
def check_password_strength(password):
    # Minimum length of 8 characters
    if len(password) < 8:
        return "Password is too short! It must be at least 8 characters long."
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    
    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."
    
    # Check for at least one special character
    if not re.search(r'[@$!%*?&]', password):
        return "Password must contain at least one special character."
    
    # If all conditions are met, the password is strong
    return "Password is strong!"

# Main function to test the password
def main():
    print("Welcome to the Password Hashing and Strength Checker!")
    
    # Ask the user for a password
    password = input("Enter a password: ")

    # Check password strength
    strength = check_password_strength(password)
    print(strength)

    if "strong" in strength.lower():
        # If the password is strong, hash it
        hashed_password = hash_password(password)
        print(f"Your hashed password (SHA-256): {hashed_password}")
    else:
        print("Please try again with a stronger password.")

if __name__ == "__main__":
    main()
