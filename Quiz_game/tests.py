# Importing the check_guess function from the main module
from game3 import check_guess

# Test case for correct guess
def test_check_guess_correct():
    assert check_guess("Beli 94,000,000.", "Beli 94,000,000.") == "Correct Answer"

# Test case for incorrect guess
def test_check_guess_incorrect():
    assert check_guess("Wrong Answer", "Beli 94,000,000.") == "The Correct answer is Beli 94,000,000."
