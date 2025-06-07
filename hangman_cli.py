import random
import string
from word_list import word_list  # External file containing list of words
from visuals import visuals_dict  # External file containing hangman visuals per chance lef

def pick_word(word_list):
    # Keep picking a random word until it contains no '-' or spaces
    while True:
        set_word = random.choice(word_list)
        if '-' not in set_word and ' ' not in set_word and set_word != '':            
            return set_word.upper()

def hangman():
    alphabet = set(string.ascii_uppercase)  # Set of all ASCII characters in uppercase
    set_word = pick_word(word_list)  # Pick a random word form word_list
    set_word_letters = set(set_word)  # Set of actual letters in the word
    guessed_letters = set()  # Set of letters guessed by the user
    chances = 7  # Number of lives
    display_word = ['_'] * len(set_word)  # List storing the updation of letters in the word

    # Game loop continues until user runs out of chances or guesses all letters
    while chances > 0 and set_word_letters:

        # Getting user input
        user_input = input('\nGuess a letter: ')
        user_input = user_input.strip().upper()

        # Validate input: must be a single letter in the alphabet
        if user_input not in alphabet or len(user_input) != 1:
            print('Invalid character!\nPlease enter a letter.\n')
            continue

        # Check if the letter was already guessed
        if user_input in guessed_letters:
            print('You have already guessed that letter.\n')
            continue

        # If the guess is wrong
        elif user_input not in set_word_letters:
            guessed_letters.add(user_input)
            print('Oh! That was a wrong guess.\nTry again.\n')
            chances = chances - 1
            print(visuals_dict[chances])

        # If the guess is correct 
        else:
            guessed_letters.add(user_input)
            print('Nice guess!')

            for index, char in enumerate(set_word):
                if char == user_input:
                    display_word[index] = user_input

            set_word_letters.remove(user_input)

        print('Current word: ', ' '.join(display_word))
        print('Remaining chances: ', chances)
        print('Guessed letters: ', ' '.join(sorted(guessed_letters)))
    # End of while loop

    # Print win/lose message
    if not set_word_letters:
        print('Congrats! You have found the word.\n')
    else:
        print('Oops! You are out of chances.\nBetter luck next time.\n')

    print('The actual word was: ', set_word) 

if __name__ == '__main__':
    while True:
        print('\nWelcome to the Hangman Game! Guess the word one letter at a time. You have 7 chances. Good luck!')
        hangman()
        again = input("Play again? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Thanks for playing!")
            break
