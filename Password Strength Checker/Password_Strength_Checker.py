import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if re.search(r'[a-z]', password):
        strength += 1

    if re.search(r'[A-Z]', password):
        strength += 1

    if re.search(r'[0-9]', password):
        strength += 1

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    return strength

    

def main():

    password = input("Enter your password: ")

    strength = check_password_strength(password)

    if strength == 5:
        print("very Strong password")
    elif strength == 4:
        print("strong password")
    elif strength == 3:
        print("moderate password")
    elif strength == 2:
        print("weak password")
    else:
        print("very weak password")   



if __name__ == '__main__':
    main()