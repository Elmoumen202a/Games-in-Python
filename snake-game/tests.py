import pytest
from unittest.mock import patch
from turtle import Vec2D
from game4 import change, inside, move, update_screen, game_over

# Mocking turtle's `bye` function to avoid actual application exit during tests
@patch('turtle.bye')
def test_game_over(mock_bye):
    """
    Test the game_over function.

    This test checks if the game_over function calls turtle.bye when executed.
    """
    game_over()
    mock_bye.assert_called_once()

def test_change_direction():
    """
    Test the change function for changing the snake direction.

    This test ensures that the change function correctly changes the direction of movement.
    """
    change(10, 0)
    assert move.direction == Vec2D(10, 0)

def test_inside_boundary():
    """
    Test the inside function for checking if a position is inside boundaries.

    This test verifies that the inside function returns True for a position within the boundaries.
    """
    assert inside(Vec2D(50, 50))

def test_outside_boundary():
    """
    Test the inside function for checking if a position is outside boundaries.

    This test checks if the inside function returns False for a position outside the boundaries.
    """
    assert not inside(Vec2D(250, 250))

@patch('turtle.clear')
@patch('turtle.update')
def test_update_screen(mock_clear, mock_update):
    """
    Test the update_screen function.

    This test mocks turtle.clear and turtle.update functions and checks if the update_screen function
    calls these turtle functions when executed.
    """
    snake = [Vec2D(10, 0), Vec2D(0, 0)]
    food = Vec2D(20, 30)
    
    update_screen(snake, food)
    
    mock_clear.assert_called_once()
    mock_update.assert_called_once()


if __name__ == '__main__':
    pytest.main()
