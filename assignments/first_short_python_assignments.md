# Quick Practice: Variables, Statements, and Functions

**Estimated time:** 45–60 minutes total
**Format:** Each problem is independent and short — a few minutes each, not a big project. Do them in order; later ones build lightly on earlier ones.

*Several of these exercises are adapted from* Think Python, 3rd Edition *by Allen B. Downey (allendowney.github.io/ThinkPython), used and adapted under a [CC BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/). This handout is shared under the same license.*

---

## Part A: Variables, Expressions, and Statements

### A1. Sphere volume
The volume of a sphere with radius `r` is `(4/3) * pi * r**3`.

Write a few lines that: create a variable `radius` set to `5`, compute the volume into a variable `volume`, and print it. Add a comment noting that `radius` is in centimeters and `volume` is in cubic centimeters. You'll need `import math` to get `math.pi`.

### A2. A trig identity
For any value of `x`, `(cos x)**2 + (sin x)**2` should equal `1`.

Create a variable `x` set to `42`, then use `math.cos` and `math.sin` to compute the sum described above and print it. It should come out very close to `1` — if it's not *exactly* `1`, that's expected; ask why, if you're curious.



### A3. One `print()`, several values
Using variables you already created above, write a single `print()` call that displays a short sentence combining at least one string and at least one number, separated by commas — e.g. something like `The volume is` followed by the number. Notice how `print` automatically adds spaces between comma-separated values.

---

## Part B: Functions

### B1. `print_right`
Write a function `print_right(text)` that prints `text` with enough leading spaces that the *last* letter lands in column 40.

```
print_right("Monty")
print_right("Python's")
print_right("Flying Circus")
```
```
                                   Monty
                                Python's
                           Flying Circus
```

*Hint: use `len()`, string concatenation (`+`), and string repetition (`*`).*

### B2. `triangle`
Write a function `triangle(character, height)` that prints a pyramid of the given height, using the given character.

```
triangle('L', 5)
```
```
L
LL
LLL
LLLL
LLLLL
```

### B3. `rectangle`
Write a function `rectangle(character, width, height)` that prints a rectangle of the given width and height.

```
rectangle('H', 5, 4)
```
```
HHHHH
HHHHH
HHHHH
HHHHH
```

### B4. Predict the error
Here's a function with a bug:

```python
def print_twice(string):
    print(cat)
    print(cat)
```

Without running it, write down: what kind of error will this cause, and why? Then run it to check. (This is the same kind of bug you'll hit constantly once you start writing bigger programs — the goal is recognizing it fast.)

---

## Part C: Putting Functions and Loops Together

### C1. Call `triangle` in a loop
Using your `triangle` function from B2, write a `for` loop that prints three triangles in a row, using heights `3`, `4`, and `5` (one call per loop iteration — don't just call `triangle` three times by hand).

### C2. `bottle_verse`
The song "99 Bottles of Beer" starts:

```
99 bottles of beer on the wall
99 bottles of beer
Take one down, pass it around
98 bottles of beer on the wall
```

Write a function `bottle_verse(n)` that prints the verse starting with `n` bottles. *Hint: write a small helper function for one line of the verse, and call it three times with different arguments inside `bottle_verse`.*

Test it with `bottle_verse(99)`. If you want to see the whole (long) song, try:

```python
for n in range(99, 0, -1):
    bottle_verse(n)
    print()
```

---

## Submission

One `.py` file with all problems in order, each labeled with a comment (`# A1`, `# A2`, `# B1`, etc.) so it's easy to find each answer.

