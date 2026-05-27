import string
import random
from datetime import datetime


length = int(input("Enter Password length: "))

password = ""

one = input("Include uppercase? (y/n): ")
two = input("Include lowercase? (y/n): ")
three = input("Include numbers? (y/n): ")
four = input("Include special characters (y/n): ")

# Build character pool dynamically
chars = ""
if one == "y":
    chars += string.ascii_uppercase
if two == "y":
    chars += string.ascii_lowercase
if three == "y":
    chars += string.digits
if four == "y":
    chars += string.punctuation

# Generate password
if not chars:
    print("You must select at least one option!")
else:
    password = "".join(random.choices(chars, k=length))
    print(f"\nGenerated password: {password}")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("passwords.txt", "a") as f:
        f.write(f"{now}: {password}\n")
    print("Password saved to passwords.txt")