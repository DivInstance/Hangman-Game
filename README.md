# Hangman-Game

Overview
Hangman is a classic word-guessing game where players attempt to deduce a hidden word by guessing letters. The game is played by one player who tries to guess the letters in a word before running out of allowed attempts.

How to Play

1.Game Start:
  a.The player is greeted and prompted to enter their name.
  b.The game explains that it will select a random word for the player to guess.

2.Game Instructions:
  a.The game displays the number of characters in the word and initializes the game with placeholders (dashes) for each letter.

3.Making Guesses:
  a.The player guesses one letter at a time.
  b.After each guess, the game informs the player if their guess was correct or incorrect.
  c.The game also keeps track of the number of guesses left.

4.Winning and Losing:
  a.The player wins if they correctly guess all the letters in the word before running out of attempts.
  b.The game ends when the player either wins or exhausts all allowed guesses, revealing the secret word if they lose.

5.Development Using Python
  The Hangman game was developed using Python with the following key components:

  Imports and Setup:

  a.The random module is used to select a random word from a predefined list.
  b.The sys module is used to exit the game if necessary.

6.Game Variables:
  wordList: A list of possible words for the game.
  secretWord: A randomly chosen word from the wordList.
  guess_word: A list of placeholders representing the letters of the secretWord.
  letter_storage: A list that keeps track of guessed letters.
  guess_taken: Counter for the number of guesses made.
  max_guesses: Maximum number of guesses allowed.

7.Functions:
  beginning(): Handles the initial greeting and name input.
  newFunc(): Introduces the game.
  change(): Initializes the guess_word with dashes and provides initial instructions.
  guessing(): Manages the guessing process, including checking for valid input and tracking the number of guesses left.
  gameLogic(): Updates the guess_word based on correct guesses and provides feedback.

8.Game Flow:
  The game starts by calling beginning() and newFunc().
  The change() function sets up the game state.
  The guessing() function runs the main game loop, handling user input and game logic.

9.Running the Game
To run the Hangman game:

  a.Ensure you have Python installed on your system.
  b.Save the provided code into a file named, for example, hangman.py.
  c.Open a terminal or command prompt and navigate to the directory containing hangman.py.
  d.Run the script using the command: python hangman.py.
  e.Follow the on-screen prompts to play the game.
