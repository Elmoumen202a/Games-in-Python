# Hangman Game
# A simple implementation of the Hangman game in Python.

# Import Statements
from random import choice
import string

# Function to Select a Word
def selectWord():
    with open("words.txt", mode="r") as w:
        wordList = w.readlines()
    return choice(wordList).strip()

# Function to Get Player's Input
def getPlayerInput(guessedLetters):
    while True:
        playerInput = input("Guess a letter: ").lower()
        if validateInput(playerInput, guessedLetters):
            return playerInput

# Function to Validate Player's Input
def validateInput(playerInput, guessedLetters):
    return (
        len(playerInput) == 1
        and playerInput in string.ascii_lowercase
        and playerInput not in guessedLetters
    )

# Function to Join Guessed Letters
def joinGuessedLetters(guessedLetters):
    return " ".join(sorted(guessedLetters))

# Function to Build Guessed Word
def buildGuessedWord(targetWord, guessedLetters):
    currentLetters = [l if l in guessedLetters else "_" for l in targetWord]
    return " ".join(currentLetters)

# Function to Draw the Hanged Man
def drawHangedMan(wrongGuesses):
    hangedMan = [  # ASCII art depicting the hangman at different stages
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        
    ]
    print(hangedMan[wrongGuesses])

# Function to Determine Game Over
MAX_INCORRECT_GUESSES = 6

def gameOver(wrongGuesses, targetWord, guessedLetters):
    if wrongGuesses == MAX_INCORRECT_GUESSES:
        return True
    if set(targetWord) <= guessedLetters:
        return True
    return False

# Main Game Loop
if __name__ == "__main__":
    # Initial setup
    targetWord = selectWord()
    guessedLetters = set()
    guessedWord = buildGuessedWord(targetWord, guessedLetters)
    wrongGuesses = 0
    print("Welcome to Hangman!")

    # Game loop
    while not gameOver(wrongGuesses, targetWord, guessedLetters):
        drawHangedMan(wrongGuesses)
        print(f"Your word is: {guessedWord}")
        print(
            "Current guessed letters: "
            f"{joinGuessedLetters(guessedLetters)}\n"
        )

        playerGuess = getPlayerInput(guessedLetters)
        if playerGuess in targetWord:
            print("Wow, great guess!")
        else:
            print("Sorry, it's not there.")
            wrongGuesses += 1

        guessedLetters.add(playerGuess)
        guessedWord = buildGuessedWord(targetWord, guessedLetters)

    # Game over
    drawHangedMan(wrongGuesses)
    if wrongGuesses == MAX_INCORRECT_GUESSES:
        print("Sorry, you lost!")
    else:
        print("Congrats! You win!")
    print(f"Your word was: {targetWord}")
