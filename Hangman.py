# The Hangman Game
import random
import sys

wordList = [
    "lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
    "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
]

guess_word = []
secretWord = random.choice(wordList)  # Randomized a single word from the list
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []
guess_taken = 0
max_guesses = int(length_word * 1.8)

def beginning():
    print("Hello Mate!\n")
    while True:
        name = input("Please enter your name\n").strip()
        if name:
            break
        else:
            print("You can't do that! No blank lines")

def newFunc():
    print("Well, that's the perfect moment to play some Hangman!\n")

def change():
    global guess_word
    guess_word = ["-" for _ in secretWord]  # Created a list of dashes for each letter in the secret word
    print("Ok, so the word you need to guess has", length_word, "characters")
    print("Be aware that you can enter only 1 letter from a-z\n\n")
    print(" ".join(guess_word))

def guessing():
    global guess_taken
    while guess_taken < max_guesses:
        print(f"Guesses left: {max_guesses - guess_taken}")
        guess = input("Pick a letter\n").lower()
        if not guess in alphabet:  # Check input validity
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage:  # Check if the letter has already been used
            print("You have already guessed that letter!")
        else:
            letter_storage.append(guess)
            gameLogic(guess)
            if not '-' in guess_word:
                print("You won!")
                break
        guess_taken += 1
    else:
        print("Sorry Mate, you lost! The secret word was", secretWord)
        print("Game Over!")
        quit()

def gameLogic(guess):
    if guess in secretWord:
        print("You guessed correctly!")
        for x in range(length_word):  # Update guess_word with the correctly guessed letter
            if secretWord[x] == guess:
                guess_word[x] = guess
        print(" ".join(guess_word))
    else:
        print("The letter is not in the word. Try again!")

beginning()
newFunc()
change()
guessing()
