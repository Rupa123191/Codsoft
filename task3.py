import random
import string

# Ask the user for the desired password length
length = int(input("Enter the desired password length: "))

# Characters to choose from (letters, numbers, and symbols)
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the generated password
print("Generated Password:", password)
