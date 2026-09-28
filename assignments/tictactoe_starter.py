# tictactoe.py
# Name:

import copy


def make_board():
    """Return a new, empty 3x3 board."""
    pass  # Step 1: replace this line with your code.


def show(board):
    """Print the board. Does not change it."""
    pass  # Step 2: replace this line with your code.


def place(board, row, col, mark):
    """Put mark at (row, col) if that square is empty.

    Changes board. Returns True if the mark was placed,
    or False (without changing anything) if the square was taken.
    """
    pass  # Step 3: replace this line with your code.


def row_winner(board, r):
    """Return the mark that fills row r, or None if nobody does."""
    # Step 4: this one is written for you. Read it, but don't change it.
    first = board[r][0]
    if first != " " and board[r][1] == first and board[r][2] == first:
        return first
    return None


def column_winner(board, c):
    """Step 5: replace this line with your own docstring."""
    pass  # Step 5: replace this line with your code.


def diagonal_winner(board):
    """Step 6: replace this line with your own docstring."""
    pass  # Step 6: replace this line with your code.


def winner(board):
    """Return "X" or "O" if that player has three in a row, else None."""
    pass  # Step 7: replace this line with your code.


def is_full(board):
    """Step 8: replace this line with your own docstring."""
    pass  # Step 8: replace this line with your code.


def empty_squares(board):
    """Return a list of [row, col] pairs for every empty square.

    Goes row by row, left to right. Does not change board.
    """
    pass  # Step 9: replace this line with your code.


def find_winning_move(board, mark):
    """Return [row, col] of a square where mark would win right away.

    Returns None if there is no such square. If there are several,
    returns the first one in empty_squares order. Does not change board.
    """
    pass  # Step 10: replace this line with your code.


def play_game():
    """Let two people play tic-tac-toe at the keyboard."""
    # Step 11: this one is written for you. Don't change it.
    board = make_board()
    mark = "X"
    while winner(board) is None and not is_full(board):
        show(board)
        print(mark + "'s turn.")
        row = int(input("Row (0, 1, or 2): "))
        col = int(input("Column (0, 1, or 2): "))
        if place(board, row, col, mark):
            if mark == "X":
                mark = "O"
            else:
                mark = "X"
        else:
            print("That square is taken. Try again.")
    show(board)
    if winner(board) is None:
        print("It's a tie!")
    else:
        print(winner(board) + " wins!")


# ---------------------------------------------------------------
# EXTRA CREDIT (optional)
# ---------------------------------------------------------------

def computer_move(board, mark):
    """Return the [row, col] the computer should play."""
    pass  # EC 1: replace this line with your code.


# EC 2: write play_vs_computer() here.


# ---------------------------------------------------------------
# MY OWN CHECKS (Steps 5, 6, and 8): once each of your checks works,
# copy it here as comments, along with the output it printed.
#
#
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# MY OWN CHECKS (Steps 5, 6 and 8): paste each of your checks
# here as comments, with what you predicted it would print and
# what it actually printed.
#
# Step 5 (column_winner):
#
#
# Step 6 (diagonal_winner):
#
#
# Step 8 (is_full):
#
#
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# REFLECTION (Step 10): write your answer as comments below.
#
#
# ---------------------------------------------------------------


# Keep this block at the very end of your file.
if __name__ == "__main__":
    # Paste the "Try it" checks from the handout here while you work.

    # When all your functions are written, take the # off the next line to play.
    # play_game()
    pass
