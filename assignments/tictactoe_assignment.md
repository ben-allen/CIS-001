# Tic-Tac-Toe

[Starter file](https://ben-allen.github.io/CIS-001/assignments/tictactoe_starter.py) 

Over the next two class sessions, you'll build a tic-tac-toe game that two people can play at the keyboard. Along the way you'll practice lists of lists, functions that change a list vs. functions that leave it alone, and docstrings.

You don't have to invent the game from scratch. You'll start from a [starter file](https://ben-allen.github.io/CIS-001/assignments/tictactoe_starter.py) that already has every function's name and (for most of them) its docstring. This handout walks you through filling in those functions one at a time. Work through them in order: each one builds on the ones before it.

**What to turn in:** your file `tictactoe.py`. If you're using Colab, remember to go to File -> Download -> Download .py

## Rules for this assignment

1. **Use exactly the function names and return types given here.** I'll test your file by importing it and calling your functions from my own code. If the names or return types don't match, my tests can't run. (The starter file already has the right names, so don't rename anything.)
2. **Every function needs a docstring.** Most are already in the starter file: leave them as they are. For three functions (`column_winner`, `diagonal_winner` and `is_full`), you'll replace the placeholder with a docstring of your own.
3. **Keep the `if __name__ == "__main__":` block at the end of your file,** so that my grading code can import your file without starting a game.

## How the board works

The board is a list of 3 rows. Each row is a list of 3 strings. Each string is `"X"`, `"O"`, or `" "` (a single space) for an empty square.

```python
board = [["X", " ", "O"],
         [" ", "X", " "],
         [" ", " ", " "]]
```

Rows and columns are both numbered 0, 1, 2. `board[row][col]` is one square, so `board[0][2]` is the top-right square, and here it's `"O"`.

```
          col 0   col 1   col 2
row 0     [0][0]  [0][1]  [0][2]
row 1     [1][0]  [1][1]  [1][2]
row 2     [2][0]  [2][1]  [2][2]
```

---

## Part 1: Warm-up questions (not scored, but do them!)

Write your answer down before running anything, then check it in Colab.

**1.** Using the `board` above, what does each line print?
```python
print(board[1][1])
print(board[0])
print(board[2][0] == " ")
print(len(board))
```

**2.** Predict the output.
```python
import copy
board = [["X", " "], [" ", " "]]
a = board.copy()
b = copy.deepcopy(board)
a[1][1] = "O"
print(board)
print(b)
```
Note: If you're confused about the difference between board.copy and copy.deepcopy(board), see week five slidesets

**3.** Write a loop that prints every square in column 1 of a board, one per line. (Hint: the row changes and the column stays the same.)

---

## Part 2: The game

### Step 0: Set up your file

Create `tictactoe.py` and paste in the **entire starter file**. It has every function you'll write, in order. Each one has its docstring and a body of just `pass`. `pass` is a placeholder that does nothing: it lets the file run before you've written the function. When you get to a function, replace its `pass` line with your code.

**Checking as you go:** each step below has a **Try it** check: a few lines of code and the output you should see. Paste the check into the `if __name__ == "__main__":` block at the bottom of your file, indented to line up with the `pass` that's already there. Run your file and compare what prints with what the handout says. Once it matches, delete the check so the output doesn't pile up.

---

### 1. `make_board()`

Returns a brand-new empty board.

**Hint:** start with an empty list and use a loop to `append` a new row `[" ", " ", " "]` three times.

**Try it:**
```python
board = make_board()
print(board)
board[0][0] = "X"
print(board)
```
You should see:
```
[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
[['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
```

---

### 2. `show(board)`

Prints the board. It doesn't return anything and doesn't change the board.

**Hints:**
- Print the line `+---+---+---+` once at the start.
- Then, for each row: print `"| " + " | ".join(row) + " |"`, followed by another `+---+---+---+` line.

**Try it:**
```python
board = make_board()
board[0][0] = "X"
board[1][1] = "O"
show(board)
```
You should see:
```
+---+---+---+
| X |   |   |
+---+---+---+
|   | O |   |
+---+---+---+
|   |   |   |
+---+---+---+
```

---

### 3. `place(board, row, col, mark)`

Puts `mark` on the board, **changing the board**. Returns `True` if it worked, or `False` if that square was already taken.

**Hint:** if `board[row][col]` isn't `" "`, return `False`. Otherwise, set the square and return `True`.

**Try it:**
```python
board = make_board()
print(place(board, 0, 2, "X"))
print(board[0][2])
print(place(board, 0, 2, "O"))
print(board[0][2])
```
You should see:
```
True
X
False
X
```

---

### 4. `row_winner(board, r)`

Returns the mark that fills all three squares of row `r`, or `None` if nobody does. **This one is already written for you** in the starter file, so you can see how it works before writing the next one yourself.

How it works: it looks at the first square of the row. If that square isn't empty, and the other two squares in the row match it, someone has filled the row.

**Try it:**
```python
board = make_board()
board[1] = ["O", "O", "O"]
print(row_winner(board, 1))
print(row_winner(board, 0))
```
You should see:
```
O
None
```

---

### 5. `column_winner(board, c)` (write your own docstring)

Returns the mark that fills all three squares of column `c`, or `None` if nobody does.

**Write this one by copying the body of `row_winner` and changing it.** In a row, the row number stays the same and the column changes. In a column, it's the other way around: `board[0][c]`, `board[1][c]`, `board[2][c]`.

**Your docstring** should say what the function returns. Use the `row_winner` docstring as your model.

**Try it:**
```python
board = make_board()
board[0][2] = "X"
board[1][2] = "X"
board[2][2] = "X"
print(column_winner(board, 2))
print(column_winner(board, 0))
```
You should see:
```
X
None
```

Write one more check of your own, using a board that tests something the checks above don't. For example, what should happen if a column has only two matching marks? Write down what it should print *before* you run it, then see if you were right.

When you're done, save your check in the **MY OWN CHECKS** section near the bottom of your file, so I can see it. Paste in the code, put a `#` at the start of each line (in Colab, select the lines and press Ctrl+/), and add two more comment lines: what you predicted it would print, and what it actually printed. For example:

```python
# board = make_board()
# board[0][0] = "O"
# print(column_winner(board, 0))
# Predicted: None
# Printed: None
```

(Your check will be different from this one!) If the two lines don't match, either your prediction or your function was wrong. Figure out which one, and fix it if it's the function.

---

### 6. `diagonal_winner(board)` (write your own docstring)

Returns the mark that fills either diagonal, or `None`.

There are two diagonals:
- `board[0][0]`, `board[1][1]`, `board[2][2]` (top-left to bottom-right)
- `board[0][2]`, `board[1][1]`, `board[2][0]` (top-right to bottom-left)

**Hint:** both diagonals go through the middle square, `board[1][1]`. If the middle is empty, nobody can have a diagonal, so return `None`. Otherwise, check whether the two corners of each diagonal match the middle.

**Your docstring** should say what the function returns.

**Try it:** (one example for each diagonal, and one with no winner)
```python
print(diagonal_winner([["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]))
print(diagonal_winner([[" ", " ", "O"], [" ", "O", " "], ["O", " ", " "]]))
print(diagonal_winner([["X", " ", " "], [" ", "X", " "], [" ", " ", "O"]]))
```
You should see:
```
X
O
None
```

Write one more check of your own. For example, what about a board where the middle square is filled but no diagonal is complete? Write down what it should print *before* you run it. Save it in the **MY OWN CHECKS** section the same way you did in Step 5.

---

### 7. `winner(board)`

Returns `"X"` or `"O"` if that player has three in a row anywhere, or `None`.

**Steps:**
1. Loop `i` over `range(3)`.
2. Inside the loop: if `row_winner(board, i)` isn't `None`, return it. Do the same for `column_winner(board, i)`.
3. After the loop, return `diagonal_winner(board)`. (If nobody has a diagonal, that's `None`, which is exactly what `winner` should return.)

**Try it:**
```python
board = make_board()
print(winner(board))
board[0][1] = "X"
board[1][1] = "X"
board[2][1] = "X"
print(winner(board))
```
You should see:
```
None
X
```

---

### 8. `is_full(board)` (write your own docstring)

Returns `True` if there are no empty squares left, or `False` otherwise.

**Hint:** loop over the rows. If `" " in row` for any row, return `False`. If the loop finishes, return `True`.

**Your docstring** should say what the function returns.

**Try it:**
```python
print(is_full([["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]))
print(is_full([["X", "O", "X"], ["X", " ", "O"], ["O", "X", "X"]]))
print(is_full(make_board()))
```
You should see:
```
True
False
False
```

**Your turn:** write one more check of your own. For example, what should happen if the only empty square is in the last row? Write down what it should print *before* you run it. Save it in the **MY OWN CHECKS** section the same way you did in Step 5.

---

### 9. `empty_squares(board)`

Returns a list of `[row, col]` pairs, one for each empty square. It doesn't change the board.

**Hint:** start with `result = []`. Use two loops, one inside the other: `r` over `range(3)`, and inside it, `c` over `range(3)`. If `board[r][c]` is empty, `append` the list `[r, c]` to `result`.

**Try it:**
```python
board = [["X", "O", "X"], [" ", "O", "O"], ["O", "X", " "]]
print(empty_squares(board))
print(len(empty_squares(make_board())))
```
You should see:
```
[[1, 0], [2, 2]]
9
```

---

### 10. `find_winning_move(board, mark)`

This one looks ahead. It returns the `[row, col]` of an empty square where `mark` could play and win immediately, or `None` if there isn't one. **It must not change the board.**

NOTE: There are many ways to solve this, but it's one of the trickier parts of the program and very easy to mess up. Following the steps below will give you a good solution. 

**Steps:**
1. Loop over `empty_squares(board)`. Each item is a `[row, col]` pair; call it `square`.
2. Make a complete copy of the board: `test = copy.deepcopy(board)`.
3. Use `place` to put `mark` on `test` at `square[0]`, `square[1]`.
4. If `winner(test) == mark`, return `square`.
5. If the loop finishes without finding a win, return `None`.

**Try it:**
```python
board = make_board()
board[0][0] = "X"
board[0][1] = "X"
print(find_winning_move(board, "X"))
print(board[0][2] == " ")
print(find_winning_move(board, "O"))
```
You should see:
```
[0, 2]
True
None
```

Notice the second line. It checks that the real board is still empty at `[0, 2]` after the function tries a move there.

**Reflection** (answer in the comment section near the bottom of the starter file): change `copy.deepcopy(board)` to `board.copy()` and run the check above again. Which line prints something different? What happened to the board, and why? Then change it back.

---

### 11. `play_game()` (already written for you)

This function uses all of yours to run a game, and it's already in the starter file. Delete any leftover checks in the `if __name__ == "__main__":` block, take the `#` off `play_game()`, run your file, and play a game!

(If you type something that isn't 0, 1, or 2, the game will crash. That's okay for now.)

---

## Checking your work

Before you turn it in, run every **Try it** check one more time and make sure each one matches. If a check prints something different from the prompt the function has a bug, even if the game seems to work. Look closely at the details: `[1, 2]` vs `[1,2]`, `None` vs nothing at all, and `True` vs `"True"` all count.

When you're done, the `if __name__ == "__main__":` block should just call `play_game()` (or `play_vs_computer()` if you did the extra credit).

---

## Extra credit: a computer player (up to [20]% extra)

### EC 1. `computer_move(board, mark)` (up to [10]%)

Returns the `[row, col]` where the computer, playing `mark`, should move. It doesn't change the board. Its docstring is already in the starter file. Use this strategy, in order:

1. If the computer can win right now, play there. (You already wrote a function for this!)
2. Otherwise, if the other player could win on their next move, play there to block them. (Same function, with the other mark.)
3. Otherwise, if the middle square is empty, take it.
4. Otherwise, take the first empty square.

**Try it:** (the first is a win, the second is a block, and the third takes the middle)
```python
print(computer_move([["O", "O", " "], ["X", "X", " "], [" ", " ", " "]], "O"))
print(computer_move([["X", "X", " "], [" ", " ", " "], [" ", " ", " "]], "O"))
print(computer_move(make_board(), "O"))
```
You should see:
```
[0, 2]
[0, 2]
[1, 1]
```

### EC 2. `play_vs_computer()` (up to [10]%)

Make a copy of `play_game` named `play_vs_computer` (there's a spot marked for it in the starter file), where you play X and the computer plays O. On O's turn, instead of asking for input, use `computer_move` to pick the square, then print where the computer played. Give it a docstring, and change the `if __name__ == "__main__":` block to call it.

Can you beat your computer player? (Hint: it isn't perfect. Try starting in a corner.)
