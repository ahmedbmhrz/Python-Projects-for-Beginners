import string
import random


def generate_password(length, include_uppercase, include_numbers, include_special ):
    if length < (include_uppercase + include_numbers + include_special):
        raise ValueError("Password length must be at least the sum of the selected character types.")
    
    
    password = ""

    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation)
    



    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    for _ in range(length - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    ''.join(password_list)
    return password



def main():
    length = int(input("enter the length of password: "))
    include_uppercase = input("Include uppercase letters (y/n)?:").lower()  == "y"
    include_numbers = input("Include numbers (y/n)?:").lower()  == "y"
    include_special = input("Include special character (y/n)?:").lower()  == "y"
    try:
        password = generate_password(length, include_uppercase, include_numbers, include_special)
        print("Generated Password: ", password)
    except ValueError as e:
        print("Error:", e)



if __name__ == "__main__":
    main()
