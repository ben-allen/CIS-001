# Python String Methods — Quick Reference

A cheat sheet of the most useful built-in string methods, with examples. Strings in Python are **immutable** — every method below returns a *new* string rather than changing the original.

```python
s = "Hello, World!"
new_s = s.upper()   # s is unchanged; new_s holds the result
```

---

## Changing Case

| Method | What it does | Example |
|---|---|---|
| `.upper()` | ALL CAPS | `"hi".upper()` → `"HI"` |
| `.lower()` | all lowercase | `"HI".lower()` → `"hi"` |
| `.title()` | Capitalizes Each Word | `"the cat".title()` → `"The Cat"` |
| `.capitalize()` | Capitalizes just the first letter | `"the cat".capitalize()` → `"The cat"` |
| `.swapcase()` | Flips upper/lower | `"Hi".swapcase()` → `"hI"` |

## Removing Whitespace

| Method | What it does | Example |
|---|---|---|
| `.strip()` | Removes whitespace from both ends | `"  hi  ".strip()` → `"hi"` |
| `.lstrip()` | Removes from the left only | `"  hi".lstrip()` → `"hi"` |
| `.rstrip()` | Removes from the right only | `"hi  ".rstrip()` → `"hi"` |

> Tip: `.strip()` can also remove specific characters: `"xxhixx".strip("x")` → `"hi"`

## Searching & Checking

| Method | What it does | Example |
|---|---|---|
| `.find(sub)` | Index of first match, or `-1` if not found | `"hello".find("l")` → `2` |
| `.index(sub)` | Like `.find()`, but raises an error if not found | `"hello".index("l")` → `2` |
| `.count(sub)` | Counts occurrences | `"hello".count("l")` → `2` |
| `.startswith(sub)` | True/False | `"hello".startswith("he")` → `True` |
| `.endswith(sub)` | True/False | `"hello".endswith("lo")` → `True` |
| `in` (keyword, not a method) | True/False | `"ell" in "hello"` → `True` |

## Checking Content Type

| Method | Checks if the string is... | Example |
|---|---|---|
| `.isalpha()` | Only letters | `"abc".isalpha()` → `True` |
| `.isdigit()` | Only digits | `"123".isdigit()` → `True` |
| `.isalnum()` | Letters and/or digits only | `"abc123".isalnum()` → `True` |
| `.isspace()` | Only whitespace | `"   ".isspace()` → `True` |
| `.islower()` | All lowercase letters | `"abc".islower()` → `True` |
| `.isupper()` | All uppercase letters | `"ABC".isupper()` → `True` |

## Splitting & Joining

| Method | What it does | Example |
|---|---|---|
| `.split()` | Splits into a list (default: on whitespace) | `"a b c".split()` → `['a', 'b', 'c']` |
| `.split(",")` | Splits on a specific character | `"a,b,c".split(",")` → `['a', 'b', 'c']` |
| `.splitlines()` | Splits on line breaks | `"a\nb".splitlines()` → `['a', 'b']` |
| `"".join(list)` | Joins a list into a string | `"-".join(['a','b'])` → `"a-b"` |

## Replacing & Building Strings

| Method | What it does | Example |
|---|---|---|
| `.replace(old, new)` | Replaces all occurrences | `"hi hi".replace("hi","bye")` → `"bye bye"` |
| `.format()` | Inserts values into placeholders | `"Hi {}".format("Sam")` → `"Hi Sam"` |
| f-strings (not a method) | Modern way to insert values | `f"Hi {name}"` |
| `.zfill(n)` | Pads with leading zeros to length `n` | `"7".zfill(3)` → `"007"` |
| `.center(n)` | Centers text in a field of width `n` | `"hi".center(6,"*")` → `"**hi**"` |

## Slicing (not a method, but essential)

```python
s = "Hello"
s[0]      # "H"      (first character)
s[-1]     # "o"      (last character)
s[1:4]    # "ell"    (characters 1 up to, not including, 4)
s[::-1]   # "olleH"  (reversed)
```

---

### Quick Practice
```python
name = "  ada lovelace  "
clean = name.strip().title()
print(clean)          # "Ada Lovelace"
print(clean.split())  # ['Ada', 'Lovelace']
```

**Remember:** Since strings are immutable, always assign the result of a method to a variable if you want to keep it!
