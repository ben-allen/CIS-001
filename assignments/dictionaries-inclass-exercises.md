# Dictionaries: In-Class Exercises


Use Think Python, Chapter 10 as a reference. For the predict-the-output questions, write your answer down before running anything, then run it to check. Drawing the arrows helps!

## Part 1: Short questions

**1.** Predict the output.

```python
born = {"Ada": 1815, "Grace": 1906}
born["Alan"] = 1912
print(len(born))
print(born["Grace"])
print("Alan" in born)
print(1815 in born)
```

**2.** Which of these lines cause an error, and what kind of error? (Think about each line on its own.)

```python
programmers = {"Ada": 137}
print(programmers["ada"])
programmers["Grace"] = 204
d = {[1, 2]: "x"}
print(programmers.get("Alan"))
```

**3.** Predict the output. 
* note: this requires stuff we'll cover on Wednesday. See [Think Python chapter 10](https://allendowney.github.io/ThinkPython/chap10.html#exercise) for info on `get` function

```python
rooms = {"Ada": 137, "Grace": 204}
print(137 in rooms)
print(137 in rooms.values())
print(rooms.get("Alan", 0))
print(rooms.get("Ada", 0))
```

**4.** Predict the output.

```python
d = {}
d["x"] = 1
d["y"] = 2
d["x"] = 3
print(d)
print(len(d))
```

**5.** Predict the output. Draw the arrows first!

```python
a = {"Ada": 1815}
b = a
c = dict(a)
b["Alan"] = 1912
c["Grace"] = 1906
print(a)
print(b)
print(c)
```

**6.** Predict the output. Which change shows up in both dictionaries, and which doesn't? Why?
* Remember: `append` changes a list by adding an element to the end.
```python
teams = {"A": ["Ada"], "B": ["Alan"]}
backup = dict(teams)
backup["A"].append("Grace")
backup["B"] = ["Katherine"]
print(teams)
print(backup)
```

**7.** Predict the output.

```python
def add_student(roster, name):
    roster[name] = 0
    roster = {}
    roster["nobody"] = 137

r = {"Ada": 98}
add_student(r, "Grace")
print(r)
```

**8.** Predict the output.

```python
counts = {"a": 3, "b": 1, "c": 2}
total = 0
for key in counts:
    total += counts[key]
    print(key, total)
```

**9.** Write a function `word_lengths(words)` that takes a list of strings and returns a dictionary that maps each word to its length. For example, `word_lengths(["Ada", "Grace", "Alan"])` returns `{'Ada': 3, 'Grace': 5, 'Alan': 4}`.

**10.** Write a function `most_common(counter)` that takes a dictionary that maps keys to counts, like the result of `value_counts`, and returns the key with the biggest count. For example, `most_common({"b": 1, "a": 3, "n": 2})` returns `"a"`. If there's a tie, returning any of the tied keys is fine.

## Part 2: The scoreboard
* This is the part you'll upload
Keep score across several games of tic-tac-toe. As in the gradebook, pay attention to which functions change the dictionary and which ones build a new one.

1. `new_scoreboard()` returns a brand-new dictionary, `{"X": 0, "O": 0, "tie": 0}`.
2. `record(scores, result)` adds 1 to the count for `result` (`"X"`, `"O"`, or `"tie"`), *in place*. It doesn't return anything.
3. `tally(results)` takes a list of results like `["X", "O", "X", "tie"]` and returns a *new* scoreboard with the totals. Use `new_scoreboard` and `record`.
4. `leader(scores)` returns `"X"` or `"O"`, whichever has more wins, or `None` if they're tied.
5. **Reflection.** Before running this code, predict what it prints and explain why. Then change one line so that `saved` keeps the old scores.

   ```python
   scores = tally(["X", "O", "X"])
   saved = scores
   record(scores, "O")
   print(saved)
   ```

### Test your functions

When all your functions are written, this code should print what the comments say.

```python
scores = tally(["X", "O", "X", "tie", "X"])
print(scores)                     # {'X': 3, 'O': 1, 'tie': 1}
print(leader(scores))             # X
record(scores, "O")
print(scores)                     # {'X': 3, 'O': 2, 'tie': 1}
print(leader(tally(["X", "O"])))  # None
print(tally([]))                  # {'X': 0, 'O': 0, 'tie': 0}
```

### Stretch

What happens if you call `record(scores, "forfeit")`? Change `record` so that a result it hasn't seen before gets added to the scoreboard with a count of 1, instead of crashing. Can you do it without an `if` statement?
