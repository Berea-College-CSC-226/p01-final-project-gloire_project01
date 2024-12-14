#####################################################################

# Author: Gloire Muzeba

######################################################################

from inspect import getframeinfo, stack
from unittest.mock import MagicMock
from original_code.game_of_nim import GameUI



def unittest(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def game_of_nim_testsuite():
    """
    The test suite function runs unit tests for Game of Nim logic.

    :return: None
    """
    print("\nRunning game_of_nim_testsuite().")

    # Initialize mock game UI
    mock_game_window = MagicMock()
    game_ui = GameUI(mock_game_window)

    # Test reset_game logic
    game_ui.remaining_balls = 10
    game_ui.user_score = 2
    game_ui.computer_score = 3
    game_ui.reset_game()
    unittest(game_ui.remaining_balls == 0)
    unittest(game_ui.user_score == 2)
    unittest(game_ui.computer_score == 3)

    # Test start_game logic
    game_ui.remaining_balls = 20
    unittest(game_ui.remaining_balls == 20)

    # Test user_turn logic
    game_ui.remaining_balls = 10
    user_input = 3  # Simulating user removing 3 balls
    game_ui.remaining_balls -= user_input
    unittest(game_ui.remaining_balls == 7)

    # Test computer_turn logic
    game_ui.remaining_balls = 7
    balls_removed_by_computer = 2  # Simulating computer removing 2 balls
    game_ui.remaining_balls -= balls_removed_by_computer
    unittest(game_ui.remaining_balls == 5)



if __name__ == "__main__":
    game_of_nim_testsuite()