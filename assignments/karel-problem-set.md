# Karel the Robot — Problem Set 1

## DUE THURSDAY, AUGUST 27, 11:59 PM

## Overview

Five required problems plus one extra-credit problem. Each is solved in the Karel
tool using `def`, `if` / `elif` / `else`, `while`, and the conditional statements below.
Read the **constraints** for each problem carefully.

## Commands available to you

```
move()              turn_left()
put_beeper()         pick_beeper()
```

## Conditional statements

```
front_is_clear()     front_is_blocked()
left_is_clear()      left_is_blocked()
right_is_clear()     right_is_blocked()
back_is_clear()      back_is_blocked()

beepers_present()    no_beepers_present()
```

## General rules

- Unless a problem says otherwise, **your solution must work in a world of
  any size**, not just the one you happened to test it in. "Works on any world"
  " and "works because I hardcoded 8 columns" look identical until you run it on
  a different world. Aside from the Maze question, your solution will only be
  tested on worlds without walls inside the world.
- The solution to the Maze assignment needs to work on **all** of the maze
  worlds I test it against. 
- Test your program against more than one world size before you consider it
  done. 

---

## Problem 1 — Row Cleanup

Karel starts at the west end of a single row of unknown length, facing east.
Beepers are scattered on some corners along the row and not on others, in no
particular pattern. Walk the row and pick up every beeper.

**Constraints**

- You don't know the row's length in advance, and you don't know which
  corners have beepers.
- Karel should end at the east end of the row (the wall), not partway
  through.
- A corner may have more than one beeper stacked on it — make sure you pick
  up all of them before moving on, not just one.

This is the warm-up: the point is a `while` loop that runs for an unknown
number of steps, driven entirely by what Karel senses underfoot and ahead 
— not by anything you counted in advance.

---

## Problem 2 — Checkerboard (One Specific World)

Fill every other corner with a beeper, in a checkerboard pattern, starting
with the corner Karel is on. This version only needs to work on the
8x8 world — you're allowed to write a solution that assumes a fixed width and
height.

**Constraints**

- Every corner of one color gets exactly one beeper; every corner of the
  other color gets none.
- It's fine if this solution breaks on a different-sized world. That's
  coming in Problem 4.

---

## Problem 3 — Maze Solving

Karel starts somewhere in a maze built from interior walls and must reach a
beeper placed elsewhere in the maze. Write a program that finds it.

**Constraints**

- You may assume the maze is a **tree**. This is a computer science term
  meaning that there are no loops in the maze's walls, so there's exactly one
  path between any two corners. 
- In other words: every corner in the maze is reachable from Karel's starting
  corner by exactly one path — there are no loops to worry about, so you'll
  never need to remember a corner you've already tried.
- Karel doesn't know which direction the beeper is in, or how far away it
  is. They only know what's immediately in front of, to the left of, and to
  the right at each step.
- Once Karel reaches the beeper, pick it up.

---

## Problem 4 — Checkerboard (Any Square World)

Same task as Problem 2 — fill alternating corners in a checkerboard pattern
— but now your program has to work on **any square world**, regardless of
its size, without modification.

**Constraints**

- Test this on at least two different square worlds, including one with an
  odd side length and one with an even side length. A solution that only
  works on even-sided worlds is the single most common bug on this problem
  — think about why row length parity (even or odd) matters here.
- Karel starts in a corner of the world, facing along one of the edges.
- You do not know the size of the world in advance. Your program has to
  discover it by sensing walls, not by being told.

---

## Problem 5 — Find the Midpoint

Karel starts at the west end of a single row of unknown length, facing
east. Place one beeper at the corner that is exactly in the middle of the
row, and nowhere else.

**Constraints**

- Think about what happens when the row has an even number of corners, so
  there is no single middle. Decide what your program should do in that
  case, and be consistent about it.
- Any beepers you may place along the way to find the middle should not still
  be on the board when you're done — only the final beeper at the midpoint
  should remain.

### A very difficult puzzle -- COMPLETELY OPTIONAL 

- If you have a working solution, a "fun" (meaning **very difficult**) puzzle
  is to write a solution that never drops any beeper except for the final one.
  Absolutely do not consider trying to find this solution, though, unless you
  have a more conventional solution that you know for a fact works.


---

## Extra Credit — World Cleanup

Beepers are scattered arbitrarily across a rectangular world of unknown
size — not just along one row, but on any corner in the grid. Gather every
beeper in the world onto the single corner in the bottom-left.

**Constraints**

- You don't know the world's width or height, or how many beepers there
  are or where they are.
- Karel needs a systematic way to visit every corner in the world — a
  back-and-forth sweep, row by row, is the standard approach. Think
  carefully about what happens at the end of each row: Karel needs to move
  up one row and reverse direction, and that "turnaround" step is where
  most attempts at this problem go wrong.
- When Karel is done, every beeper in the world should be on the
  bottom-left corner, and nowhere else.

This one is meaningfully harder than the required problems — it's a genuine
step up in difficulty, not just a longer version of Row Cleanup. Attempt it
only after the required problems are solid.



# KAREL REFERENCE SHEET

## While loops

    while front_is_clear():
        move()

Repeats the indented block for as long as the condition is true. Karel
checks the condition before each pass — including the first — so if it's
already false, the body never runs at all.

## if / elif / else

    if beepers_present():
        pick_beeper()
    elif front_is_clear():
        move()
    else:
        turn_left()

Karel checks the conditions in order, top to bottom, and runs the first
block whose condition is true — the rest are skipped. `elif` and `else`
are both optional; use only what the problem needs. `else` runs whenever
none of the conditions above it were true, and takes no condition itself.

## Defining new functions

    def turn_right():
        turn_left()
        turn_left()
        turn_left()

Teaches Karel a new command, built from ones they already know. Once
defined, call it exactly like a built-in: `turn_right()`. Definitions go
above `main()`, not inside another function.
