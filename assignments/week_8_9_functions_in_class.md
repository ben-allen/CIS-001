# CIS001 Week 8-9 In-Class: Doing Things with Functions

Note: [These are the slides](https://ben-allen.github.io/CIS-001/slides/cis001_week_8_tuples_functions.pdf) associated with this assignment.

## How to work through this

Many of these questions ask you to **predict first, then run**. Write your prediction down *before* you run the code. Getting a prediction wrong is fine, and it's how you'll learn the most today. When a prediction is wrong, take a moment to work out *why* before you move on.

If you get stuck, open the **Hint** under the question. Try for a couple of minutes before you open it.

## Part 1: Calls inside calls (review)

Remember from the slides:

- **Chaining** (`a.strip().lower()`) reads **left to right**. Each method is called on whatever the one before it returned.
- **Nesting** (`dict(zip(a, b))`) reads **inside out**. The innermost call runs first, and its result becomes the argument to the next call out.

### Question 1: Trace a chain

```python
name = "  grace HOPPER "
print(name.strip().lower().split())
```

**a)** Fill in this table, one row for each method call. The first row is done for you.

| Step | Called on | Returns |
|---|---|---|
| `.strip()` | `"  grace HOPPER "` | `"grace HOPPER"` |
| `.lower()` | | |
| `.split()` | | |

**b)** Predict what the `print` line prints. Then run it.

**c)** Now add these lines and predict what they print:

```python
first, last = name.strip().lower().split()
print(last.upper())
```

<details><summary>Hint</summary>
For (c): the chain gives back a list with two strings in it, and tuple assignment unpacks that list into <code>first</code> and <code>last</code>, the same as <code>user, domain = email.split("@")</code> on the slides.
</details>

### Question 2: Inside out

For each line, first write down **which call runs first**, then predict what gets printed.

```python
print(max(len("Ada"), len("Grace")))
print(len(str(2 ** 10)))
print(list(zip("ab", [1, 2])))
```

<details><summary>Hint</summary>
In the second line, start from the innermost part: what is <code>2 ** 10</code>? What does <code>str</code> turn it into? How many characters does that have?
</details>

### Question 3: Squish it into one line

This code works, but it takes six lines:

```python
clock = " 09:45 "
clock = clock.strip()
parts = clock.split(":")
minutes = parts[1]
minutes = int(minutes)
print(minutes + 15)
```

**a)** Predict what it prints.

**b)** Write **one line** that gives `minutes` the same value, starting from the original `clock`. Check it by printing `minutes + 15`.

**c)** A classmate's one-line version leaves out `int`. Predict what happens when they print `minutes + 15`, then try it and copy down the error message.

<details><summary>Hint</summary>
Do the chain first: <code>strip</code>, then <code>split</code>, then the indexing <code>[1]</code>. That gives you the string <code>"45"</code>. To turn it into a number, the whole chain has to go <em>inside</em> <code>int( )</code>. That part is nesting, so it reads inside out.
</details>

### Question 4: The chain that breaks

```python
names = ["Grace", "Ada", "Alan"]
result = names.sort()
print(result)
print(names)
```

**a)** Predict both lines, then run them. (Think back to the lists deck: what does `sort` *return*?)

**b)** Now predict what this does:

```python
names.sort().reverse()
```

Run it and copy down the error message. In your own words, explain **why** this chain breaks when `strip().lower()` didn't.

**c)** What does `sorted(names)[0]` give you? Why does this one work?

<details><summary>Hint</summary>
A chain only works if every step <em>returns</em> something you can keep working with. <code>sort</code> changes the list in place and returns <code>None</code>, so <code>.reverse()</code> gets called on <code>None</code>. <code>sorted</code> returns a brand-new list.
</details>

---

## Part 2: A function is a value

Remember from the slides:

- `shout` (no parentheses) **is the function itself**. You can store it, give it another name, or pass it to another function.
- `shout("hi")` (with parentheses) **calls** it: the function runs right now and you get back what it returns.
- `key=` hands `sorted`, `max`, and `min` a function. **They** call it, once for each item.

### Question 5: Warm-up predictions

```python
def double(n):
    return n * 2

twice = double

print(twice(5))
print(double(twice(5)))
print(double)
print(double())
```

**a)** Predict each line. One of them prints something odd, and one of them is an error. Which is which?

**b)** Draw the arrows for `twice = double`. How many function objects are there?

**c)** For each of these, write **function** or **call**: `double`, `double(4)`, `twice`, `print`, `print("hi")`, `len`.

### Question 6: Built-in functions are values too

You don't have to write your own function to use `key=`. Any function that takes one argument will do, including built-ins like `len`.

```python
words = ["banana", "fig", "apple", "kiwi"]
print(sorted(words))
print(sorted(words, key=len))
print(max(words, key=len))
print(min(words, key=len))
```

**a)** Before predicting, fill in this table. It's what `sorted` actually looks at when `key=len`:

| item | `len(item)` |
|---|---|
| `"banana"` | |
| `"fig"` | |
| `"apple"` | |
| `"kiwi"` | |

**b)** Now predict all four lines, then run them.

**c)** Methods are functions too. Try this:

```python
print(str.lower("HeLLo"))

people = ["ada", "Grace", "alan", "Bob"]
print(sorted(people))
print(sorted(people, key=str.lower))
```

Predict, then run. Why does `sorted(people)` put `"Bob"` and `"Grace"` first? What did `key=str.lower` change?

<details><summary>Hint</summary>
Python compares letters by their character codes, and every uppercase letter comes before every lowercase letter. <code>str.lower</code> is the same <code>lower</code> you've been chaining, just written without the dot in front and without the parentheses, so it's the method itself rather than a call to it. <code>sorted</code> calls it on each name and sorts by the lowercased version. The names themselves don't change.
</details>

### Question 7: Write your own key functions

Here's a list of tuples: (name, birth year, city).

```python
people = [
    ("Grace", 1906, "New York"),
    ("Katherine", 1918, "Charleston"),
    ("Ada", 1815, "London"),
    ("Alan", 1912, "London"),
]
```

**a)** Fill in the blank so `year` returns the birth year from one tuple:

```python
def year(person):
    return ____
```

Test it: `year(("Ada", 1815, "London"))` should give `1815`.

**b)** Use `sorted` with `key=year` to print the people from oldest to youngest.

**c)** Use `min` with `key=year` to find the oldest person. Then **unpack** the result into three variables and print just the name:

```python
name, born, city = ____
print(name)
```

**d)** Write a function `name_length(person)` that returns how many letters are in the person's name. Use it with `max` to find the person with the longest name.

**e) Bug hunt.** A classmate wrote this:

```python
print(sorted(people, key=year()))
```

Predict the error *before* you run it. Then run it and read the message carefully. Is it complaining about `sorted` or about `year`? Fix it.

<details><summary>Hint</summary>
For (d): the name is <code>person[0]</code>, and you want <code>len</code> of that. That's a nested call, from Part 1!<br>
For (e): look at the parentheses after <code>year</code>. When does <code>year()</code> run, and what argument does it get?
</details>

### Question 8: A function that takes a function

So far `sorted` and `max` have done the calling. Now **you** write the function that receives another function and calls it.

Here's a test function. It answers a yes/no question about one word:

```python
def is_long(word):
    return len(word) > 4
```

**a)** Fill in the blank. `count_if` should count how many items pass `test`:

```python
def count_if(items, test):
    count = 0
    for item in items:
        if ____:
            count += 1
    return count

words = ["banana", "fig", "apple", "kiwi"]
print(count_if(words, is_long))
```

Predict the output before you run it.

**b)** Write your own test function `starts_with_a(word)` that returns `True` if the word starts with `"a"`. What does `count_if(words, starts_with_a)` give?

**c)** Now write `keep(items, test)`. Instead of counting, it returns a **new list** of the items that pass the test. It has the same shape as `count_if`, but uses a list instead of a counter.

```python
print(keep(words, is_long))        # should print ['banana', 'apple']
print(keep(words, starts_with_a))  # should print ['apple']
```

**d)** `count_if` and `keep` work on any list, not just words. Write `born_before_1900(person)` for the `people` list from Question 7, and use `keep` to get everyone born before 1900.

<details><summary>Hint</summary>
For (a): inside <code>count_if</code>, the function you passed in is named <code>test</code>. Call it the way you'd call any function: <code>test(item)</code>. That's the same move as <code>f(x)</code> inside <code>apply_twice</code> on the slides.<br>
For (c): start with <code>result = []</code>, <code>append</code> each item that passes, and <code>return result</code> after the loop.<br>
For (d): <code>person[1]</code> is the year.
</details>

### Question 9: Composition, as a function

Part 1 was all about composition: one function's output becomes the next function's input. Here it is written as a function:

```python
def compose(f, g, x):
    return f(g(x))

def add_one(n):
    return n + 1

def shout(s):
    return s.upper() + "!"
```

**a)** Trace `compose(double, add_one, 3)` by hand. What are `f`, `g`, and `x`? Which function runs first? What's the final answer?

**b)** Predict `compose(add_one, double, 3)`. Is it the same as (a)? What does this tell you about the order of `f` and `g`?

**c)** Predict, then run:

```python
print(compose(shout, str.strip, "  hi  "))
print(compose(len, double, "hi"))
```

(Remember what `*` does to a string. `double` doesn't care whether you give it a number or a string.)

**d)** Write the first line of (c) **without** `compose`, as a nested call.

<details><summary>Hint</summary>
<code>f(g(x))</code> is inside out: <code>g</code> runs first, on <code>x</code>, and then <code>f</code> runs on whatever <code>g</code> returned.
</details>

---

## Stretch: Question 10, a pipeline

*Only if you finish early. It's fine to stop before this.*

What if you want to run *more* than two functions, one after another? You could put the functions in a list:

```python
def run_pipeline(x, steps):
    for step in steps:
        x = step(x)
    return x
```

**a)** Trace `run_pipeline(3, [add_one, double, double])` by hand. Write down the value of `x` after each time through the loop.

**b)** Predict `run_pipeline(3, [double, double, add_one])`. Same steps, different order: same answer?

**c)** Predict `run_pipeline(3, [])`. Why?

**d)** Here's the email chain from the slides, `"  Ada@Python.org ".strip().lower()`, rewritten as a pipeline. Predict the output:

```python
print(run_pipeline("  Ada@Python.org ", [str.strip, str.lower]))
```

**e)** Make your own pipeline that starts with `"  ada  "` and ends with the number `4`. You can use `str.strip`, `shout`, `len`, or any function you wrote today.

---

## Before you go

Write one or two sentences answering this: **what's the difference between `key=year` and `key=year()`?** If you can explain that clearly, you understood today.
