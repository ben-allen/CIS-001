# Lists: In-Class Exercises

CIS001 · Think Python, Chapter 9


Part 1 is a set of short questions to check that you've got the ideas from today. For the predict-the-output questions, write your answer down before running anything, then check it in Colab. Drawing the arrows helps!

## Part 1: Short questions

**1.** Predict the output.

```python
t = [10, 20, 30, 40]
print(t[1:3])
print(t[-1])
print(len([1, [2, 3], 4]))
print(3 in [1, [2, 3], 4])
```

**2.** Which of these lines cause an error, and what kind of error?

```python
word = "cat"
word[0] = "b"
nums = [1, 2, 3]
nums[0] = 9
print(nums[5])
```

**3.** Predict the output. Draw the arrows first!

```python
a = [1, 2]
b = a
c = a[:]
b.append(3)
c.append(4)
print(a)
print(b)
print(c)
```

**4.** Predict the output of each snippet.

```python
x = [1, 2]
y = x
x += [3]
print(y)
```

```python
s = "ab"
t = s
s += "c"
print(t)
```

**5.** For each `print`, say whether it prints `True` or `False`.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)
print(a is b)
print(a is c)
```

**6.** Predict the output.

```python
def change(lst):
    lst[0] = 99
    lst = [0, 0]
    lst.append(5)

nums = [1, 2, 3]
change(nums)
print(nums)
```

**7.** This code crashes. Explain why, then fix it.

```python
names = ["Anna", "Bob"]
names = names.append("Charli")
print(len(names))
```

**8.** Write a function `count_long(words, n)` that takes a list of strings and returns how many of them are longer than `n` characters. For example, `count_long(["hi", "hello", "hey"], 2)` returns `2`.

**9.** Write a function `initials(name)` that takes a full name and returns its initials as one string. For example, `initials("Ada King Lovelace")` returns `"AKL"`. Use `split`.

## Part 2: The gradebook

Write the functions below. Pay close attention to which ones should change the list and which ones should leave it alone. That difference is the whole point of this exercise.

1. `parse_scores(text)` takes a string like `"88 92 75 64 100"` and returns a list of ints, `[88, 92, 75, 64, 100]`. Use `split`, a loop, `int`, and `append`.
2. `average(scores)` returns the average of the scores.
3. `above(scores, cutoff)` returns a *new* list of the scores greater than `cutoff`. The original list must not change.
4. `curve(scores, points)` adds `points` to every score *in place*, capping each score at 100. It doesn't return anything. Hint: loop over `range(len(scores))` so you can assign to `scores[i]`.
5. `curved(scores, points)` does the same thing, but returns a *new* list and leaves the original alone.
6. `drop_lowest(scores)` removes the lowest score from the list *in place*. Hint: `min` and `remove`.
7. **Reflection.** Before running this code, predict what it prints and explain why. Then change one line so that `backup` keeps the original scores.

   ```python
   scores = parse_scores("88 92 75 64 100")
   backup = scores
   curve(scores, 5)
   print(backup)
   ```

### Test your functions

When all your functions are written, this code should print what the comments say.

```python
scores = parse_scores("88 92 75 64 100")
print(average(scores))        # 83.8
print(above(scores, 80))      # [88, 92, 100]
print(scores)                 # [88, 92, 75, 64, 100], unchanged
print(curved(scores, 5))      # [93, 97, 80, 69, 100]
print(scores)                 # still unchanged
curve(scores, 5)
print(scores)                 # [93, 97, 80, 69, 100]
drop_lowest(scores)
print(scores)                 # [93, 97, 80, 100]
```

### Stretch

Write `report(scores)`, which returns a string like `"88, 92, 75, 64, 100"`. Try `", ".join(scores)` first and see what happens. Why doesn't it work, and how can you fix it?
