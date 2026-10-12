# Tuples: In-Class Exercises

These exercises practice the tuple material from Think Python, Chapter 11: making tuples, immutability, tuple assignment, `zip` and `enumerate`, and sorting with a `key`. **Part 2 is the part you upload:** submit `seating.py` by Monday, October 19.

Work out every Part 1 question on paper first, *then* check your answers in Colab. When a question says to draw the references, draw the arrows: most of the surprises in this chapter only make sense in the picture.

## Part 1: Short questions

**1. Predict the output.**

```python
person = ("Grace", "Hopper", 1906)
print(person[1])
print(person[-1])
print(person[:2])
print(len(person))
print("Hopper" in person)
print(1906 in person[:2])
```

**2. What type is each variable: `tuple`, `str`, `int`, or `list`?** For each tuple, also write out what it looks like when printed.

```python
a = ("Ada")
b = ("Ada",)
c = "Ada", "Grace"
d = (1815)
e = tuple("Ada")
f = ["Ada"]
g = ()
```

**3. Find the errors.** Each line starts fresh with `t = ("Ada", 1815)`, i.e. assume that each line is being run in a separate Colab code window, immediately after `t = ("Ada", 1815)`. For each line, say whether it works. If it doesn't, name the error (`TypeError`, `AttributeError`, `ValueError`, ...) and explain why in one sentence.

```python
t[1] = 1816
t.append("London")
t = t + ("London",)
t = t + "London"
name, year, city = t
seats = {(3, 7): "Ada"}
seats = {[3, 7]: "Ada"}
teams = {("Ada", ["Grace"]): 1}
```

**4. Predict the output. Draw the references first.**

```python
a = ("Ada", ["Grace"])
b = a
b[1].append("Alan")
b = b + ("Katherine",)
print(a)
print(b)
```

**5. Predict the output.**

```python
x, y, z = 1, 2, 3
x, y, z = z, x, y
print(x, y, z)

first, last = "Margaret Hamilton".split()
print(last, first)
```

**6. Predict the output.**

```python
rooms = {"Ada": 137, "Grace": 204}
for name, room in rooms.items():
    print(room, name)

for i, letter in enumerate("hi"):
    print(i, letter)

print(list(zip("abc", [1, 2, 3, 4])))
```

**7. Predict the output.** For each comparison, say which elements decided the answer.

```python
print((1, 2, 3) < (1, 3))
print(("Grace", 1906) < ("Ada", 1815))
print((2, "a") < (2, "b"))
print(sorted([(2, "b"), (1, "z"), (2, "a")]))
```

**8. Explain and fix.** This code is supposed to find the person born earliest, but it crashes. Explain what went wrong, then fix it by changing one line. What does the fixed version give for `oldest`?

```python
def second_element(t):
    return t[1]

born = {"Ada": 1815, "Grace": 1906, "Alan": 1912}
oldest = min(born.items(), key=second_element())
```

**9. Write `first_and_last(t)`.** It takes any sequence and returns a tuple of its first and last elements. Then use tuple assignment to unpack the result into two variables.

```python
print(first_and_last([86, 94, 75]))    # (86, 75)
print(first_and_last("python"))        # ('p', 'n')
low, high = first_and_last((1815, 1906, 1912))
print(low, high)                       # 1815 1912
```

**10. Write `count_matches(word1, word2)`.** It returns how many positions have the same letter in both words. Use `zip`; if the words have different lengths, ignore the extra letters.

```python
print(count_matches("tuple", "table"))  # 3
print(count_matches("abc", "abcd"))     # 3
print(count_matches("ada", "bob"))      # 0
```

## Part 2: The seating chart

You'll write a small program that keeps track of who sits where in a classroom. Put all of your functions in one file named `seating.py`, and give every function a docstring.

A **seat** is a tuple `(row, seat_number)`. Rows and seats are both numbered from 1, and row 1 is at the front. A **chart** is a dictionary that maps each seat to the name of the person sitting there:

```python
chart = {(1, 1): "Alan", (1, 2): "Grace", (2, 1): "Ada"}
```

Watch which functions change the chart they're given and which ones build something new. The instructions for each function say which kind it is.

**1. `make_chart(names, seats)`.** Takes a list of names and a list of seats in the same order. Returns a **new** chart where each seat maps to the name at the same position. Hint: `zip` and `dict` can do this in one line.

**2. `seat_of(chart, name)`.** Returns the seat where `name` is sitting, or `None` if they aren't in the chart. Loop over `chart.items()` and unpack each item in the `for` line. Doesn't change the chart.

**3. `swap_seats(chart, seat1, seat2)`.** Swaps the people sitting in `seat1` and `seat2`. This one **changes the chart in place** and returns nothing. You can assume both seats have someone in them. Write the swap in one line, with tuple assignment.

**4. `seating_order(chart)`.** Returns a **new** list of names in seating order: front row first, and left to right (by seat number) within each row. Hint: what order does `sorted(chart.items())` put the items in, and why? Doesn't change the chart.

**5. `row_names(chart, row)`.** Returns a **new** list of the names in one row, in order of seat number. If nobody sits in that row, return an empty list. Hint: unpack each seat into its row and seat number, collect `(seat_number, name)` tuples for the matching row, then sort them. Doesn't change the chart.

**6. Reflection.** Predict what this prints and explain why in two or three sentences. Then change one line so that `saved` keeps the original seating.

```python
chart = make_chart(["Ada", "Grace"], [(1, 1), (1, 2)])
saved = chart
swap_seats(chart, (1, 1), (1, 2))
print(saved[(1, 1)])
```

**7. Reflection.** Why are seats tuples, and not lists like `[1, 2]`? Answer in one or two sentences.

## Test your functions

Paste this at the bottom of `seating.py` and run it. Each comment shows what that line should print. Check the last two lines carefully: `swap_seats` should return `None`, and building the chart shouldn't change `names`.

```python
if __name__ == "__main__":
    names = ["Ada", "Grace", "Alan", "Katherine", "Margaret"]
    seats = [(2, 1), (1, 2), (1, 1), (2, 3), (2, 2)]
    chart = make_chart(names, seats)

    print(chart)
    # {(2, 1): 'Ada', (1, 2): 'Grace', (1, 1): 'Alan', (2, 3): 'Katherine', (2, 2): 'Margaret'}
    print(seat_of(chart, "Katherine"))   # (2, 3)
    print(seat_of(chart, "Charles"))     # None
    print(seating_order(chart))           # ['Alan', 'Grace', 'Ada', 'Margaret', 'Katherine']
    print(row_names(chart, 2))            # ['Ada', 'Margaret', 'Katherine']
    print(row_names(chart, 5))            # []

    result = swap_seats(chart, (1, 1), (2, 3))
    print(seating_order(chart))           # ['Katherine', 'Grace', 'Ada', 'Margaret', 'Alan']
    print(result)                         # None
    print(names)                          # ['Ada', 'Grace', 'Alan', 'Katherine', 'Margaret']
```

## Finally

Write `fullest_row(chart)`. It returns a tuple `(row, count)` for the row with the most people in it. If two rows tie, either one is fine.

First count the people in each row, using a dictionary that maps row numbers to counts. Then find the row with the largest count by calling `max` on that dictionary's items with a `key` function. You'll need to write the `key` function yourself.

```python
print(fullest_row(chart))   # (2, 3) with the chart from the test script
```
