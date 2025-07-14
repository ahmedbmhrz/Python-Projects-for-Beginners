import random

def generate_secret():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(digits)
    secret = ''
    for digit in digits[:4]:
        secret += str(digit)
    return secret

def calculate_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def main():
    secret = generate_secret()
    while True:
        guess = input('Guess a 4 digit number: ')
        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
            cows , bulls = calculate_bulls_and_cows(secret, guess)
            print(f'Cows: {cows}, Bulls: {bulls}')

            if bulls == 4:
                print('Congratulations! You guessed the number!')
                break
        else:
            print('Invalid input. Please enter a 4 digit number with no repeating digits.')


if __name__ == '__main__':
    main()