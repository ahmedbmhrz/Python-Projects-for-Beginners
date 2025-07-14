import random

def generate_secret():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(str(digit) for digit in digits[:4])

def calculate_bulls_and_cows(secret, guess):
    bulls = sum([1 for i in range(4) if guess[i] == secret[i]]) 
    cows = sum([1 for i in range(4) if guess[i] in secret]) - bulls
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