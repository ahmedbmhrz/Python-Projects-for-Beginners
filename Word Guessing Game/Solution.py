import random
import re

def read_words():
    try:
        with open("words.txt", "r") as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print("Error: words.txt not found.")
        return []

def display_word(secret_word, guessed_letters):
    word_to_display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            word_to_display += letter
        else:
            word_to_display += "_"
    print(word_to_display)

def get_guess(guessed_letters):
    while True:
        guess = input('Guess a letter:').lower()
        if len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        elif not re.search(r'[a-z]', guess):
            print("Invalid input. Please enter a letter from a to z.")
            continue
        elif guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        else:
            return guess

def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True
            


def main():
    words = read_words()
    if not words:
        print("No words to choose from.")
        return
    secret_word = random.choice(words)
    print(secret_word)

    guessed_letter = []
    attempts = 6
    while attempts > 0:
        display_word(secret_word,guessed_letter)

        guess = get_guess(guessed_letter)
        guessed_letter.append(guess)

        if guess in secret_word:
            print("Correct!")
            if is_word_guessed(secret_word, guessed_letter):
                print("Congratulations! You guessed the word:", secret_word)
                break

        else:
            print("Incorrect.")
            attempts -= 1
            print("Attempts remaining:", attempts)
            if attempts == 0:
                print("Sorry, you ran out of attempts. The word was:", secret_word)


if __name__ == "__main__":
    main()