from game2 import play_rock_paper_scissors

def test_play_rock_paper_scissors():
    assert play_rock_paper_scissors("rock") in ["Player 1 Won", "Player 2 Won", "Tie"]
    assert play_rock_paper_scissors("paper") in ["Player 1 Won", "Player 2 Won", "Tie"]
    assert play_rock_paper_scissors("scissor") in ["Player 1 Won", "Player 2 Won", "Tie"]

