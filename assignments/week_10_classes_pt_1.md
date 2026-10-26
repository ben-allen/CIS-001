# Assignment: Working with Dates

**Covers:** Think Python chapter 14 (classes and functions) and the week 8 slides, plus earlier chapters.

**Points:** 15

**Due:** Monday, November 2

**Submit:** your finished `dates.py`

In the slides we built a `Time` class and wrote functions that make, print, change, and copy `Time` objects. In this assignment you'll do the same for calendar dates. Dates are trickier than times: months have different lengths, and February depends on the year.

Start from the provided `dates.py`. Don't change any function names or parameters, because the test scripts call them exactly as written. Code you use to try things out goes inside the `if __name__ == "__main__":` block at the bottom, and nowhere else.

Don't use Python's `datetime` or `calendar` modules. The only import you need is `copy`, which is already in the file.

## Part 1: the class and the basics (3 points)

1. Write a class called `Date` that represents a date on the calendar. Like `Time` in the slides, its body only needs a docstring.
2. `make_date(year, month, day)` makes a `Date`, gives it attributes named `year`, `month`, and `day`, and returns it.
3. `date_to_iso(date)` returns the date in ISO form, `YYYY-MM-DD`. March 7, 2026 is `'2026-03-07'`. Pad the year to 4 digits and the month and day to 2, using `zfill` like the slides do.
4. `date_to_us(date)` returns the date in U.S. form, `MM/DD/YYYY`. March 7, 2026 is `'03/07/2026'`. Pad the same way.
5. `print_date(date)` prints the date in ISO form. Use `date_to_iso` instead of repeating the work.

## Part 2: calendar rules (4 points)

6. `is_leap_year(year)` takes an int and returns `True` or `False`. The full rule:
   - A year divisible by 4 is a leap year,
   - except a year divisible by 100 is not,
   - except a year divisible by 400 is.

   So 2024 and 2000 are leap years; 2026 and 1900 are not.
7. `days_in_month(date)` returns how many days are in the date's month:

   | Month | Days | Month | Days |
   |---|---|---|---|
   | 1 January | 31 | 7 July | 31 |
   | 2 February | 28, or 29 in a leap year | 8 August | 31 |
   | 3 March | 31 | 9 September | 30 |
   | 4 April | 30 | 10 October | 31 |
   | 5 May | 31 | 11 November | 30 |
   | 6 June | 30 | 12 December | 31 |
8. `is_valid(date)` returns `True` if the date really exists. `make_date(2026, 2, 29)` and `make_date(2026, 13, 1)` are not valid.
9. `same_date(date1, date2)` returns `True` if the two dates have the same year, month, and day.
10. `is_after(date1, date2)` returns `True` if `date1` is later on the calendar than `date2`. (Hint: chapter 11 shows how Python compares tuples.)
11. `increment_date(date)` changes `date` to the next day and returns nothing. It moves forward **one day only**. December 31, 2026 becomes January 1, 2027, and February 28 becomes February 29 or March 1 depending on the year.
12. `next_day(date)` returns a **new** `Date` for the following day and leaves `date` unchanged. Use `copy` and `increment_date`.
13. `days_until(date1, date2)` counts how many days it takes to step from `date1` to `date2`, using a loop. You can assume `date2` is the same as `date1` or after it. It must not change `date1`.

You can assume every `Date` passed to the functions in steps 7 and 9–13 is valid.

## Part 3: questions (3 points)

Answer the four questions in the comments near the bottom of `dates.py`. Short answers are fine, but explain *why*, not just *what*.

## Testing your work

Before you submit, try at least these in your `__main__` block:

- Is 1900 a leap year? 2000? 2024? 2026?
- What do `date_to_iso` and `date_to_us` give for 2026-03-07? For 2026-12-25?
- What comes after 2024-02-28? After 2026-02-28? After 2026-12-31?
- `days_until` from 2026-01-01 to 2027-01-01 should be 365. From 2024-01-01 to 2025-01-01 it should be 366.
- After calling `next_day(d)`, print `d`. Did it change? (It shouldn't.)
