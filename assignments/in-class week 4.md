# In-Class Exercises: Return Values, Conditionals, and Strings

*Covers* Think Python *(3rd ed.), Chapters 1–6, plus string methods and slicing*

**Time:** about 90 minutes to 2 hours (but I'm bad at estimating things)

Work through the exercises in order. Exercises 1–6 are the core set. Exercises 7 and 8 are stretch problems. The times are rough guides: if you've been stuck on one part for more than 10 minutes, ask for help or move on and come back.

## Ground rules

1. **Use the main guard.** Put your function definitions at the top of your code. Put all test calls inside an `if __name__ == "__main__":` block at the bottom, like this:

   ```python
   def double(x):
       return x * 2

   if __name__ == "__main__":
       print(double(4))    # expect 8
       print(double(-1))   # expect -2
   ```

2. **Return, don't print.** Unless an exercise says otherwise, your functions should `return` their result. Do your printing in the main block.
3. **Develop incrementally.** Write a few lines, run them, check the result, then add more. Printing intermediate values is a good way to check your progress. Remove those extra prints when you're done.
4. **No recursion** is required in today's solutions.
5. **Test beyond the examples.** Each exercise gives some example calls with expected results. Test those, then add at least one test case of your own.

## Exercise 1: Distance between points 

Write a function `distance(x1, y1, x2, y2)` that returns the distance between the points (x1, y1) and (x2, y2):

distance = √((x2 − x1)² + (y2 − y1)²)

Use incremental development:

1. Write a version that just returns `0.0`, and confirm it runs.
2. Compute `dx` and `dy`, and print them to check them.
3. Compute the sum of the squares, and print it.
4. Take the square root with `math.sqrt` and return the result.

| Call | Expected result |
|---|---|
| `distance(0, 0, 3, 4)` | `5.0` |
| `distance(1, 2, 1, 2)` | `0.0` |
| `distance(-1, -1, 2, 3)` | `5.0` |


## Exercise 2: Boolean functions 

Write each of these functions so that it returns `True` or `False`. For a challenge, write each function body as a single `return` statement.

**a)** `is_between(x, y, z)` returns `True` if `x <= y <= z`.

| Call | Expected result |
|---|---|
| `is_between(1, 2, 3)` | `True` |
| `is_between(1, 1, 1)` | `True` |
| `is_between(3, 2, 1)` | `False` |

**b)** `is_leap_year(year)` returns `True` if `year` is a leap year. A year is a leap year if it is divisible by 4, *except* years divisible by 100 are not leap years, *unless* they are also divisible by 400.

| Call | Expected result |
|---|---|
| `is_leap_year(2024)` | `True` |
| `is_leap_year(2023)` | `False` |
| `is_leap_year(1900)` | `False` |
| `is_leap_year(2000)` | `True` |

**Question:** Why is `if is_leap_year(y) == True:` unnecessary? What's the simpler way to write it?

## Exercise 3: Letter grades 

Write `letter_grade(score)`, which takes a number from 0 to 100 and returns a letter grade as a string:

| Score | Grade |
|---|---|
| 90 and above | `"A"` |
| 80–89 | `"B"` |
| 70–79 | `"C"` |
| 60–69 | `"D"` |
| below 60 | `"F"` |

Use a chained conditional (`if` / `elif` / `else`). Then add input validation: if `score` is not an `int` or `float` (check with `isinstance`), or if it is outside the range 0–100, return `None`.

| Call | Expected result |
|---|---|
| `letter_grade(95)` | `"A"` |
| `letter_grade(80)` | `"B"` |
| `letter_grade(59.9)` | `"F"` |
| `letter_grade(105)` | `None` |
| `letter_grade("90")` | `None` |

**Question:** Does the order of your conditions matter? What would happen if you checked `score >= 60` first?

## Exercise 4: Slicing practice 

**a)** `middle(word)` returns `word` without its first and last characters.

| Call | Expected result |
|---|---|
| `middle("python")` | `"ytho"` |
| `middle("ab")` | `""` |

**b)** `is_palindrome(word)` returns `True` if `word` reads the same forwards and backwards, ignoring uppercase and lowercase. Use slicing, not recursion.

| Call | Expected result |
|---|---|
| `is_palindrome("Racecar")` | `True` |
| `is_palindrome("noon")` | `True` |
| `is_palindrome("python")` | `False` |
| `is_palindrome("")` | `True` |

**c)** `mask_card(number)` takes a credit-card number as a string and returns a version in which every character except the last four is replaced by `*`. If the string has four or fewer characters, return it unchanged.

| Call | Expected result |
|---|---|
| `mask_card("1234567812345678")` | `"************5678"` |
| `mask_card("9876")` | `"9876"` |

*Hint:* What does `"*" * 3` evaluate to?

## Exercise 5: Making usernames 

Write `make_username(first, last, year)`, which builds a username from:

- the first letter of `first`,
- the first **seven** letters of `last` (or all of `last`, if it's shorter),
- the last two digits of `year` (an `int`).

The whole username should be lowercase.

| Call | Expected result |
|---|---|
| `make_username("Ada", "Lovelace", 1815)` | `"alovelac15"` |
| `make_username("Alan", "Turing", 1912)` | `"aturing12"` |
| `make_username("GRACE", "Hopper", 2006)` | `"ghopper06"` |
| `make_username("Bo", "Li", 1999)` | `"bli99"` |

*Hints:* What happens when a slice goes past the end of a string? How can you get the last two digits of `year` as a string? Watch out for the `2006` case.

## Exercise 6: Password checker 

Write `is_strong_password(pw)`, which returns `True` only if **all** of these conditions are met:

- `pw` is at least 8 characters long,
- it contains at least one uppercase letter,
- it contains at least one lowercase letter,
- it contains at least one character that is not a letter.

You can solve this with string methods alone: no loops. Think about what `pw.lower() == pw` tells you, and look up `isalpha` in your string-method reference.

| Call | Expected result |
|---|---|
| `is_strong_password("Secret123")` | `True` |
| `is_strong_password("secret123")` | `False` |
| `is_strong_password("SECRET123")` | `False` |
| `is_strong_password("SecretPass")` | `False` |
| `is_strong_password("Ab1")` | `False` |

**Then:** Write `password_feedback(pw)`, which returns a string describing the **first** requirement the password fails (for example, `"Too short"`). If the password passes every requirement, return `"Strong password"`. You decide the exact messages.

## Stretch Exercise 7: Triangle classifier 

Write `triangle_type(a, b, c)`, which takes three side lengths and returns:

- `None` if any argument isn't an `int` or `float`, or if any side is ≤ 0,
- `"not a triangle"` if any one side is greater than or equal to the sum of the other two,
- `"equilateral"` if all three sides are equal,
- `"isosceles"` if exactly two sides are equal,
- `"scalene"` otherwise.

| Call | Expected result |
|---|---|
| `triangle_type(3, 3, 3)` | `"equilateral"` |
| `triangle_type(3, 3, 5)` | `"isosceles"` |
| `triangle_type(3, 4, 5)` | `"scalene"` |
| `triangle_type(1, 2, 3)` | `"not a triangle"` |
| `triangle_type(3, 4, -5)` | `None` |
| `triangle_type(3, "4", 5)` | `None` |

**Hint:** Consider writing a helper function `is_triangle(a, b, c)` and calling it from `triangle_type`.

## Stretch Exercise 8: 12-hour to 24-hour time (≈15 min)

Write `to_24_hour(time_str)`, which converts a time like `"7:05 PM"` into 24-hour format like `"19:05"`.

- The input always has the form *hours*`:`*minutes*, a space, then `AM` or `PM`. The hour may have one or two digits.
- The output always has two digits for the hour and two for the minutes.
- `12:xx AM` is `00:xx`, and `12:xx PM` stays `12:xx`.

| Call | Expected result |
|---|---|
| `to_24_hour("7:05 PM")` | `"19:05"` |
| `to_24_hour("11:30 AM")` | `"11:30"` |
| `to_24_hour("12:00 AM")` | `"00:00"` |
| `to_24_hour("12:45 PM")` | `"12:45"` |
| `to_24_hour("1:00 AM")` | `"01:00"` |

*Hints:* `find` can tell you where the colon and the space are. `int()` turns a string into a number, and `str()` turns a number back into a string. `zfill` is also worth looking up.

**Extra challenge:** Write the reverse function, `to_12_hour("19:05")`, which returns `"7:05 PM"`.

