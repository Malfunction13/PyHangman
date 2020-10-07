"""Simple hangman game"""
import random
import json
import re
from HangmanGraphic import *

data = json.load(open("words.json"))
word = random.choice(list(data.values()))


name = input("Please insert your name: ")
greeting = "Welcome, %s! Lets play a deadly game!" % name.title()
print(greeting)
print("=" * len(greeting))
print("You have to guess the word in 9 attempts or this poor man here will hang!")



# Generate new words until the user decides to quit, keep track of lives left,correct and wrong guesses
while True:

    correct_guesses = []
    wrong_guesses = []
    failed_attempts = 0
    lives_left = 9
    random_word = random.choice(word).lower()

    print("=" * len(greeting))
    print("The word you have to guess has {} letters and you have {} lives left!\nLet the hanging begin!"
          .format(len(random_word), lives_left))
    print("=" * len(greeting))
    print(*(i for i in (re.sub('[a-z]', '_', random_word))), sep=" ")

    # Ask the user to guess a letter until 0 lives left and check scenarios
    while lives_left > 0:

        hidden_word = ""
        guess = input("Guess a letter: ").lower()

        # If the input is incorrect the user will be asked to guess again
        if len(guess) > 1 or not guess.isalpha():
            print("Please insert only 1 letter at a time from A-Z!")

        # if the letter has already been guessed the user will be asked to guess again
        if guess in correct_guesses:
            print("Already guessed, try again!")

        # If the input is correct
        if guess.isalpha() and len(guess) == 1:

            # If the guessed letter is in the word and is not already guessed
            if guess in random_word and guess not in correct_guesses:
                for i in range(random_word.count(guess)):
                    correct_guesses.append(guess)
                print("You have guessed correctly:", *correct_guesses)
                print("Congratulations your guess was CORRECT!")

                # Display updated hidden version
                for letter in random_word:
                    if letter in correct_guesses:
                        hidden_word += letter
                    else:
                        hidden_word += "_"
                print(*(i for i in hidden_word), sep=" ")

                # If the result is same as the word you win!
                if hidden_word.strip() == random_word:

                    print("YOU DID IT YOU BASTARD!\nYou win!")

            # If guess not in the word 1 life will be lost and scenarios will be checked
            if guess.isalpha() and guess not in random_word:
                lives_left -= 1
                failed_attempts += 1
                wrong_guesses.append(guess)
                draw_hangman(failed_attempts)

                print("Sorry, your guess was WRONG! You lose 1 life!\nYou have {} lives left".format(lives_left))
                print("Wrong letters:", *wrong_guesses)

            # If the user is out of lives
            if lives_left == 0:
                print("You loose, but the hanging man lost more! HA - HA - HAaaa!")
                print("The word was %s!" %random_word.upper())
                # ask user to play again and check the input
        # asking to retry
        if lives_left == 0 or hidden_word.strip() == random_word:
            while True:
                print("Would you like to try again?")
                play_again = input("Press Y for YES and N for NO: ")
                if play_again == "y":
                    lives_left = 0
                    break

                elif play_again not in ["y", "n"]:
                    print("Wrong input!")
                    play_again
                else:
                    print("Thank you for playing PyHangman!")
                    exit()
