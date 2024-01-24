# Function to check the user's guess against the correct answer
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 4:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again: ")
            attempt += 1
    if attempt == 3:
        print("The Correct answer is", answer)

# Main function to execute the One Piece guessing game
def main():
    global score
    score = 0
    print("Guess One Piece")
    
    # Asking questions and checking answers
    guess1 = input("What is the bounty of 'Rookie' Rockstar? ")
    check_guess(guess1, "Beli 94,000,000.")

    guess2 = input("Who of the eleven Supernovas ate a Zoan Devil Fruit? ")
    check_guess(guess2, "X Drake")

    guess3 = input("What is the name of the mayor of Luffy's hometown? ")
    check_guess(guess3, "Woop Slap")

    guess4 = input("What does the name 'Kuja' mean? ")
    check_guess(guess4, "Nine snakes")

    print("Your Score is " + str(score))

# Entry point of the script
if __name__ == "__main__":
    main()
