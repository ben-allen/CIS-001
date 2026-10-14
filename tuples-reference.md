# Week 7 Reference Sheet: Tuples

## Making and using tuples

| What | What it does | Example |
|---|---|---|
| `(a, b, c)` | Makes a tuple. The commas make it a tuple; the parentheses are optional | `person = ("Ada", 1815)` |
| `(x,)` | A one-element tuple needs a trailing comma. `("Ada")` is just a string | `one = ("Ada",)` |
| `()` | The empty tuple | `empty = ()` |
| `tuple(seq)` | Makes a tuple from any sequence | `tuple("abc")` → `('a', 'b', 'c')` |
| `t[i]`, `t[i:j]`, `len(t)`, `x in t`, `for x in t` | Work the same as on lists | `person[0]` → `'Ada'` |
| `t1 + t2`, `t * n` | Build a **new** tuple. The original never changes | `("Ada",) + ("London",)` |
| `type(x)` | Tells you what kind of value `x` is | `type(("Ada",))` → `<class 'tuple'>` |

**Remember:** tuples are immutable. You can't assign to an element (`t[0] = ...` is a TypeError), and tuples have no `append` or `remove`. But a mutable object *inside* a tuple, like a list, can still change.

**Tuples as keys:** a tuple can be a dictionary key, as long as everything inside it is immutable. `seats[3, 7] = "Ada"` is the same as `seats[(3, 7)] = "Ada"`.

## Tuple assignment (unpacking)

| What | What it does | Example |
|---|---|---|
| `a, b = seq` | Gives each variable the value in the same position | `name, year = "Ada", 1815` |
| `a, b = b, a` | Swaps two variables. The whole right side is worked out first | |
| `for k, v in ...:` | Unpacks each tuple as you loop | `for name, room in rooms.items():` |
| `return x, y` | Returns two values packed into one tuple | `low, high = min_max(scores)` |

If the number of variables doesn't match the number of values, you get `ValueError: too many values to unpack` or `not enough values to unpack`.

## Functions and methods

| Name | What it does | Example |
|---|---|---|
| `d.items()` | A dictionary's (key, value) pairs, as tuples | `list({"a": 1}.items())` → `[('a', 1)]` |
| `divmod(a, b)` | Returns `(a // b, a % b)` together | `q, r = divmod(7, 3)` → `2`, `1` |
| `zip(s1, s2)` | Pairs up elements, one from each sequence. Stops when the shorter one runs out | `list(zip("ab", [1, 2]))` → `[('a', 1), ('b', 2)]` |
| `enumerate(seq)` | Gives (index, element) pairs, starting at 0 | `for i, name in enumerate(names):` |
| `dict(pairs)` | Makes a dictionary from a sequence of pairs | `dict(zip(names, years))` |
| `list(x)` | Makes a list from a sequence. Use it to see what's in a zip or items | `list(zip(names, years))` |
| `sorted(seq)` | Returns a new sorted list. Tuples sort by first element, then second, and so on | `sorted(counts.items())` |
| `sorted(seq, key=f)` | Sorts by what `f` returns for each element | `sorted(counts.items(), key=second_element)` |
| `max(seq, key=f)`, `min(seq, key=f)` | The element where `f` gives the largest or smallest result | `max(born.items(), key=second_element)` |
| `s.strip()` | String with leading and trailing spaces removed | `"  hi ".strip()` → `'hi'` |
| `s.lower()`, `s.upper()` | String in all lowercase or all uppercase | `"Ada".lower()` → `'ada'` |
| `s.split(sep)` | Splits a string into a list of strings | `"a@b.org".split("@")` → `['a', 'b.org']` |

## Packing and unpacking arguments with `*`

| What | What it does | Example |
|---|---|---|
| `def f(*args):` | Packs any number of arguments into one tuple | `def mean(*args): return sum(args) / len(args)` |
| `f(*seq)` | Unpacks a sequence into separate arguments | `mean(*[86, 94, 75])` |

## Comparing tuples

Python compares tuples element by element, left to right. The first pair of elements that differ decides the result, and nothing after that is looked at.
`(0, 1, 2000000) < (0, 3, 4)` is `True`, because `1 < 3` decides it.

## Functions as values

- **Calls inside calls (composition):** `dict(zip(names, years))` runs from the inside out. `zip` runs first, and its result goes to `dict`.
- **Chaining:** `email.strip().lower().split("@")` runs left to right. Each method is called on what the one before it returned.
- **A function is a value:** `shout` is the function itself, and `shout("hi")` *calls* it. `yell = shout` gives the same function a second name.
- **Passing a function:** you can pass a function to another function, which calls it later.
  ```python
  def apply_twice(f, x):
      return f(f(x))
  apply_twice(double, 3)   # → 12
  ```
- **No parentheses when passing:** use `key=second_element`, not `key=second_element()`. With the parentheses, the function is called right away with no arguments, and you get a TypeError.
