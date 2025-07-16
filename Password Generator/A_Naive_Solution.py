import string
import random


def generate_password(length, include_uppercase, include_numbers, include_special ):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    length = int(input("enter the length of password: "))
    include_uppercase = input("Include uppercase letters (y/n)?:").lower()  == "y"
    include_numbers = input("Include numbers (y/n)?:").lower()  == "y"
    include_special = input("Include special character (y/n)?:").lower()  == "y"

    password = generate_password(length, include_uppercase, include_numbers, include_special)

    print("Generated Password: ", password)



if __name__ == "__main__":
    main()
