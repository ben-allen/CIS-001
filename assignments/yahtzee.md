# Yahtzee: Project Assignment

## Overview

You'll build a playable, one-player version of the dice game Yahtzee, one small function at a time. By the end, you'll run `play_game()` and play a full 13-turn game against your own code.

This project is bigger than anything you've written so far, but you won't have to figure out how to break it into pieces. That part is done for you: every function you need is listed below, in the order you should write it, with a test for each one. Your job is to write each function, check it against its test, and only then move on. If you work in order and test as you go, no single step is hard.

**What to turn in:** one `.py` file containing all the functions in Stages 1 to 5, plus your answers to the Reflection questions as comments at the top of the file.

**IMPORTANT: USE EXACTLY THE SAME FUNCTION NAMES, PARAMETERS, AND RETURN TYPES AS IN THE SPECIFICATION.** I'll test your code by calling your functions from my own test program. If a name or return type doesn't match, my tests can't run.

### The rules (our version)

A game lasts 13 turns. On each turn:

1. Roll all five dice.
2. You may reroll any of the dice you like, keeping the rest. You can do this up to two times, so a turn has at most three rolls in total.
3. Choose one category on your scorecard to score these dice in. Each category can only be used once per game, so after 13 turns every category is filled. If the dice don't fit the category you pick, you score 0 there. Sometimes that's the smart move.

The 13 categories:

| Category | Scores | Example dice | Points |
| --- | --- | --- | --- |
| ones, twos, threes, fours, fives, sixes | Total of only the dice showing that number | `[3, 3, 5, 2, 3]` in threes | 9 |
| three of a kind | Total of all five dice, if at least three are the same | `[3, 3, 5, 2, 3]` | 16 |
| four of a kind | Total of all five dice, if at least four are the same | `[6, 6, 6, 6, 2]` | 26 |
| full house | 25, if three of one number and two of another | `[2, 5, 2, 5, 5]` | 25 |
| small straight | 30, if four numbers in a row appear anywhere | `[3, 4, 5, 3, 6]` | 30 |
| large straight | 40, if five numbers in a row | `[5, 3, 2, 4, 6]` | 40 |
| yahtzee | 50, if all five dice are the same | `[6, 6, 6, 6, 6]` | 50 |
| chance | Total of all five dice, no conditions | `[1, 4, 2, 6, 6]` | 19 |

**Upper bonus:** if the six number categories (ones through sixes) add up to 63 or more, you get 35 bonus points.

The order of the dice never matters. `[5, 3, 2, 4, 6]` is a large straight even though it isn't written in order.

## The plan

The program is 24 small functions, most under 10 lines. Big functions get short by calling small ones. For example, `score_full_house` will be about three lines long because `counts` does the hard work. When you get to a function, look at the "Uses" column: those are the helpers you should call instead of starting from scratch.

As in the gradebook assignment, pay close attention to the "Changes the list?" column. Only three functions are allowed to change the list they're given. Every other function must leave its argument exactly as it found it.

| Function | Stage | Changes the list? | Returns | Uses |
| --- | --- | --- | --- | --- |
| `roll_dice(n)` | 1 | (makes a new one) | list of ints | `random.randint` |
| `reroll(dice, positions)` | 1 | **Yes** | nothing | `random.randint` |
| `parse_positions(text)` | 1 | No | list of ints |  |
| `show_dice(dice)` | 1 | No | string |  |
| `total(dice)` | 2 | No | int |  |
| `count(dice, value)` | 2 | No | int |  |
| `counts(dice)` | 2 | No | list of 6 ints | `count` |
| `has_run(dice, length)` | 2 | No | bool | `counts` |
| `score_upper(dice, value)` | 3 | No | int | `count` |
| `score_three_kind(dice)` | 3 | No | int | `counts`, `total` |
| `score_four_kind(dice)` | 3 | No | int | `counts`, `total` |
| `score_full_house(dice)` | 3 | No | int | `counts` |
| `score_small_straight(dice)` | 3 | No | int | `has_run` |
| `score_large_straight(dice)` | 3 | No | int | `has_run` |
| `score_yahtzee(dice)` | 3 | No | int | `counts` |
| `score_chance(dice)` | 3 | No | int | `total` |
| `score_for(dice, category)` | 4 | No | int | all the `score_` functions |
| `new_scorecard()` | 4 | (makes a new one) | list |  |
| `record(scorecard, category, dice)` | 4 | **Yes** (the scorecard) | nothing | `score_for` |
| `available(scorecard)` | 4 | No | list of strings |  |
| `upper_total(scorecard)` | 4 | No | int |  |
| `upper_bonus(scorecard)` | 4 | No | int | `upper_total` |
| `total_score(scorecard)` | 4 | No | int | `upper_bonus` |
| `play_turn(scorecard)` | 5 | **Yes** (the scorecard, via `record`) | nothing | almost everything |

### How to work

1. Put `import random` at the very top of your file, and copy in the provided code from Stage 4 (`CATEGORIES`) and Stage 5 (`show_scorecard` and `play_game`).
2. Write one function.
3. Run its test code. Compare your output to the comments line by line.
4. Only when it matches, move to the next function.

If you're stuck on a function, it's fine to skip it and come back, as long as nothing later in the list uses it. The "Uses" column tells you what depends on what.

## Stage 1: The dice

The dice are just a list of five ints, like `[3, 3, 5, 2, 3]`. To roll one die, use `random.randint(1, 6)`, which returns a random int from 1 to 6 (including both 1 and 6). You need `import random` at the top of your file.

**1. `roll_dice(n)`** returns a new list of `n` random dice. Start with an empty list, loop `n` times, and `append` a `random.randint(1, 6)` each time.

**2. `reroll(dice, positions)`** rerolls some of the dice **in place**. `positions` is a list of indexes, like `[0, 2]`. Each die at one of those indexes gets a new random value; every other die stays exactly the same. It doesn't return anything. Hint: loop over `positions`, and for each index `i`, assign to `dice[i]`.

**3. `parse_positions(text)`** turns what the player types into a list of indexes. Players count dice starting from 1, but Python counts from 0, so `parse_positions("1 3 5")` returns `[0, 2, 4]`. This is almost the same as `parse_scores` from the gradebook: `split`, loop, `int`, `append`. The only difference is subtracting 1. What does your function return for `""` (an empty string)? It should return `[]`, and if you used `split`, it already does.

**4. `show_dice(dice)`** returns a string that shows each die with its position number, so the player knows what to type. `show_dice([3, 3, 5, 2, 3])` returns `"1:3  2:3  3:5  4:2  5:3"` (two spaces between each pair). Hint: build a list of strings like `"1:3"`, then use `"  ".join(...)`. Remember what you learned in the gradebook stretch problem about `join` and ints.

### Test Stage 1

Because the dice are random, these tests check what *must* be true rather than exact values.

```python
dice = roll_dice(5)
print(len(dice))                   # 5
print(min(dice) >= 1)              # True
print(max(dice) <= 6)              # True

dice = [1, 1, 1, 1, 1]
result = reroll(dice, [0, 2])
print(result)                      # None
print(dice[1], dice[3], dice[4])   # 1 1 1   (these must not change)
print(len(dice))                   # 5

print(parse_positions("1 3 5"))    # [0, 2, 4]
print(parse_positions("2"))        # [1]
print(parse_positions(""))         # []

print(show_dice([3, 3, 5, 2, 3]))  # 1:3  2:3  3:5  4:2  5:3
```

## Stage 2: Counting helpers

These four functions don't score anything by themselves. They're the tools that make Stage 3 easy. None of them may change `dice`.

**5. `total(dice)`** returns the sum of all the dice. Write it with a loop and an accumulator, not the built-in `sum`, just this once.

**6. `count(dice, value)`** returns how many dice show `value`. `count([3, 3, 5, 2, 3], 3)` returns `3`. Write it with a loop, the same pattern as `count_long` from Part 1 of the lists exercises. (Python lists have a `.count` method that does this, but write it yourself.)

**7. `counts(dice)`** returns a list of six ints: how many ones, how many twos, and so on up to sixes. `counts([3, 3, 5, 2, 3])` returns `[0, 1, 3, 0, 1, 0]`, meaning zero ones, one two, three threes, zero fours, one five, zero sixes. Watch the off-by-one: the count of *threes* is at index **2**. Hint: loop `value` from 1 to 6 with `range(1, 7)` and append `count(dice, value)` each time.

`counts` is the most important function in the project. Look at `[0, 1, 3, 0, 1, 0]` and notice how easy it is to answer questions like "are there three of a kind?" (is some count at least 3?) or "is this a yahtzee?" (is some count equal to 5?).

**8. `has_run(dice, length)`** returns `True` if the dice contain `length` numbers in a row, and `False` otherwise. `has_run([3, 4, 5, 3, 6], 4)` is `True`, because 3, 4, 5, 6 all appear. Hint: a run of 4 exists if some slice of `counts(dice)` with 4 entries contains no zeros. For a run of 4, check the slices starting at index 0, 1, and 2. In general, loop `start` over `range(7 - length)` and, with `c = counts(dice)`, check whether `0 in c[start:start + length]`.

### Test Stage 2

```python
dice = [3, 3, 5, 2, 3]
print(total(dice))                     # 16
print(count(dice, 3))                  # 3
print(count(dice, 4))                  # 0
print(counts(dice))                    # [0, 1, 3, 0, 1, 0]
print(counts([6, 6, 6, 6, 6]))         # [0, 0, 0, 0, 0, 5]
print(dice)                            # [3, 3, 5, 2, 3], unchanged

print(has_run([3, 4, 5, 3, 6], 4))     # True
print(has_run([3, 4, 5, 3, 6], 5))     # False
print(has_run([5, 3, 2, 4, 6], 5))     # True
print(has_run([1, 2, 3, 5, 6], 4))     # False
```

## Stage 3: Scoring

Each of these functions takes a list of five dice and returns an int: the number of points those dice would earn in one category (see the rules table in the Overview). If the dice don't qualify, it returns `0`. None of them may change `dice`.

If you did Stage 2 well, most of these are one to three lines. If one of yours is getting long, stop and look at the "Uses" column in the plan again.

**9. `score_upper(dice, value)`** returns the total of only the dice showing `value`. `score_upper([3, 3, 5, 2, 3], 3)` returns `9`. Hint: how many threes are there, and what is each worth? This one function handles all six upper categories.

**10. `score_three_kind(dice)`** returns the total of all the dice if at least three are the same, otherwise `0`. Hint: with `c = counts(dice)`, three of a kind means the largest number in `c` is at least 3.

**11. `score_four_kind(dice)`** is the same idea with four.

**12. `score_full_house(dice)`** returns `25` if the dice are three of one number and two of another, otherwise `0`. Hint: look at `counts([2, 5, 2, 5, 5])`. What two numbers must be *in* the counts list?

**13. `score_small_straight(dice)`** returns `30` if there's a run of 4, otherwise `0`.

**14. `score_large_straight(dice)`** returns `40` if there's a run of 5, otherwise `0`.

**15. `score_yahtzee(dice)`** returns `50` if all five dice are the same, otherwise `0`.

**16. `score_chance(dice)`** returns the total of all the dice.

### A warning about sorting

You might be tempted to sort the dice to check for straights. Don't call `dice.sort()` inside any of these functions: it rearranges the player's actual dice, and the positions they see on screen will suddenly be wrong. If you really want sorted dice, `sorted(dice)` returns a *new* sorted list and leaves `dice` alone. (But with `has_run`, you don't need to sort at all.) Reflection question 1 asks you about this.

### Test Stage 3

```python
print(score_upper([3, 3, 5, 2, 3], 3))       # 9
print(score_upper([3, 3, 5, 2, 3], 4))       # 0

print(score_three_kind([3, 3, 5, 2, 3]))     # 16
print(score_three_kind([2, 5, 2, 5, 5]))     # 19
print(score_three_kind([1, 2, 3, 4, 5]))     # 0
print(score_four_kind([6, 6, 6, 6, 2]))      # 26
print(score_four_kind([3, 3, 5, 2, 3]))      # 0

print(score_full_house([2, 5, 2, 5, 5]))     # 25
print(score_full_house([3, 3, 5, 2, 3]))     # 0
print(score_full_house([6, 6, 6, 6, 6]))     # 0   (five of a kind is not a full house)

print(score_small_straight([3, 4, 5, 3, 6])) # 30
print(score_large_straight([3, 4, 5, 3, 6])) # 0

dice = [5, 3, 2, 4, 6]
print(score_large_straight(dice))            # 40
print(score_small_straight(dice))            # 30  (a large straight contains a small one)
print(dice)                                  # [5, 3, 2, 4, 6], unchanged, NOT sorted

print(score_yahtzee([6, 6, 6, 6, 6]))        # 50
print(score_yahtzee([6, 6, 6, 6, 2]))        # 0
print(score_four_kind([6, 6, 6, 6, 6]))      # 30  (a yahtzee also counts as four of a kind)

print(score_chance([1, 4, 2, 6, 6]))         # 19
```

## Stage 4: The scorecard

The scorecard is a list of 13 values, one per category, in the same order as this list. **Copy this line into your program exactly as written:**

```python
CATEGORIES = ["ones", "twos", "threes", "fours", "fives", "sixes",
              "three of a kind", "four of a kind", "full house",
              "small straight", "large straight", "yahtzee", "chance"]
```

So `scorecard[2]` is the score for "threes", and `scorecard[8]` is the score for "full house". To find the index of a category, use `CATEGORIES.index(category)`. For example, `CATEGORIES.index("full house")` is `8`.

An unused category holds `None`, not `0`. That's because scoring 0 is a real move in Yahtzee: if you're forced to put `[1, 2, 2, 4, 6]` somewhere, you might take a 0 in yahtzee. `None` means "not used yet"; `0` means "used, and scored nothing." To check for it, write `if value is None:`.

**17. `score_for(dice, category)`** takes a category name (a string from `CATEGORIES`) and returns what these dice would score there. It doesn't record anything. It's a long `if`/`elif` chain that calls the right Stage 3 function, for example `elif category == "full house": return score_full_house(dice)`. For the six upper categories, you can write six branches, or you can be clever: if `category in CATEGORIES[:6]`, the value you want is `CATEGORIES.index(category) + 1`.

**18. `new_scorecard()`** returns a new list of 13 `None`s. Hint: `[None] * len(CATEGORIES)`.

**19. `record(scorecard, category, dice)`** scores the dice in that category and stores the result in the scorecard, **in place**. It doesn't return anything. It's two lines: find the right index, then assign `score_for(...)` there. You can assume the category is valid and unused; `play_turn` will check that before calling `record`.

**20. `available(scorecard)`** returns a new list of the names of all categories that are still `None`. Hint: loop over `range(len(scorecard))`, and when `scorecard[i] is None`, append `CATEGORIES[i]`.

**21. `upper_total(scorecard)`** returns the total of the first six entries (ones through sixes), counting `None` as 0.

**22. `upper_bonus(scorecard)`** returns `35` if `upper_total` is at least 63, otherwise `0`.

**23. `total_score(scorecard)`** returns the total of every entry that isn't `None`, plus the upper bonus.

### Test Stage 4

```python
print(score_for([3, 3, 5, 2, 3], "threes"))          # 9
print(score_for([3, 3, 5, 2, 3], "full house"))      # 0
print(score_for([2, 5, 2, 5, 5], "full house"))      # 25
print(score_for([6, 6, 6, 6, 6], "sixes"))           # 30

card = new_scorecard()
print(card)                   # [None, None, None, None, None, None, None, None, None, None, None, None, None]

record(card, "threes", [3, 3, 5, 2, 3])
record(card, "full house", [2, 5, 2, 5, 5])
record(card, "chance", [6, 6, 5, 4, 6])
print(card)                   # [None, None, 9, None, None, None, None, None, 25, None, None, None, 27]
print(available(card))        # ['ones', 'twos', 'fours', 'fives', 'sixes', 'three of a kind', 'four of a kind', 'small straight', 'large straight', 'yahtzee']
print(upper_total(card))      # 9
print(upper_bonus(card))      # 0
print(total_score(card))      # 61

card2 = new_scorecard()
record(card2, "ones", [1, 1, 1, 2, 3])
record(card2, "twos", [2, 2, 2, 1, 1])
record(card2, "threes", [3, 3, 3, 1, 1])
record(card2, "fours", [4, 4, 4, 1, 1])
record(card2, "fives", [5, 5, 5, 1, 1])
record(card2, "sixes", [6, 6, 6, 1, 1])
print(upper_total(card2))     # 63
print(upper_bonus(card2))     # 35
print(total_score(card2))     # 98
print(card[0])                # None  (card2 is a separate list; card didn't change)
```

## Stage 5: The game

This stage turns your functions into a game you can actually play. Two functions are provided; copy them into your program as written. You write the third, `play_turn`.

### Provided code

```python
def show_scorecard(scorecard):
    lines = []
    for i in range(len(CATEGORIES)):
        value = scorecard[i]
        if value is None:
            value = "-"
        lines.append(f"{CATEGORIES[i]:>16}: {value}")
    lines.append(f"{'upper bonus':>16}: {upper_bonus(scorecard)}")
    lines.append(f"{'TOTAL':>16}: {total_score(scorecard)}")
    return "\n".join(lines)


def play_game():
    scorecard = new_scorecard()
    for turn in range(len(CATEGORIES)):
        print()
        print(f"===== Turn {turn + 1} of {len(CATEGORIES)} =====")
        play_turn(scorecard)
    print()
    print(show_scorecard(scorecard))
    print("Game over! Final score:", total_score(scorecard))
```

Notice that `play_game` never assigns a new value to `scorecard`. It creates one list at the start and passes that same list to `play_turn` 13 times. That only works because `play_turn` (through `record`) changes the list in place.

### 24. `play_turn(scorecard)`

Plays one full turn: rolling, rerolling, and choosing a category. It changes `scorecard` in place and returns nothing. Almost all the real work is done by functions you've already written, so each step below should be only one to four lines. Copy this skeleton and replace each comment with code:

```python
def play_turn(scorecard):
    # Step 1: Roll five dice and store them in a variable called dice.

    # Step 2: Let the player reroll, up to two times.
    for roll in range(2):
        # a. Print the dice using show_dice.
        # b. Use input() to ask which dice to reroll, e.g.
        #    "Positions to reroll (e.g. 1 3 5), or Enter to keep all: "
        # c. Turn the answer into a list of indexes with parse_positions.
        # d. If that list is empty, the player is happy: use break to stop rerolling.
        # e. Otherwise, reroll those positions.
        pass   # delete this line once you've written the steps

    # Step 3: Print the final dice and the current scorecard (show_scorecard).

    # Step 4: For each category in available(scorecard), print its name
    #         and what these dice would score there (score_for), e.g.
    #         "  full house: 25"

    # Step 5: Ask the player which category to use.
    #         Keep asking (a while loop) until the answer is in available(scorecard).

    # Step 6: Record the dice in that category.
```

When it works, a turn will look something like this (your wording can differ):

```text
===== Turn 4 of 13 =====
1:2  2:5  3:5  4:1  5:5
Positions to reroll (e.g. 1 3 5), or Enter to keep all: 1 4
1:2  2:5  3:5  4:2  5:5
Positions to reroll (e.g. 1 3 5), or Enter to keep all:
Final dice: 1:2  2:5  3:5  4:2  5:5
...
  three of a kind: 19
  full house: 25
  chance: 19
...
Which category? full house
```

Finally, run `play_game()` and play a whole game. Your score goes in Reflection question 4.

## Reflection

Answer these as comments at the top of your file. For the predict-the-output questions, write your prediction down before running anything.

**1. The sorting bug.** A classmate wrote this version of `score_large_straight`:

```python
def score_large_straight(dice):
    dice.sort()
    if dice == [1, 2, 3, 4, 5] or dice == [2, 3, 4, 5, 6]:
        return 40
    return 0

dice = [5, 3, 2, 4, 6]
print(show_dice(dice))
print(score_large_straight(dice))
print(show_dice(dice))
```

(a) Predict all three lines of output. (b) Their function passes the scoring tests. Explain why it would still confuse a player during a real game. (c) Fix it by changing **one line** of the function, without using `has_run`. Hint: remember Question 6 from the lists exercises, where assigning to a parameter didn't affect the caller's list.

**2. The disappearing scorecard.** Suppose someone changes one line of `play_game` to this:

```python
        scorecard = play_turn(scorecard)
```

Predict what happens when they play. Does the first turn work? What about the second? Explain which earlier exercise this reminds you of.

**3. Why the helpers?** Suppose we add a new category, "two pairs": the total of all five dice if at least two different numbers each appear two or more times, otherwise 0. So `[4, 4, 1, 6, 6]` scores 21, and `[4, 4, 4, 6, 6]` scores 24. Write `score_two_pairs(dice)`. How many lines did it take? How many would it have taken without `counts`?

**4. Play!** Play at least one full game. Report your final score, and describe one turn where you deliberately took a 0 or a low score in some category, and why.

## Stretch (for a small amount of extra credit)

Only start these once everything above works.

**A. A hint button.** Write `best_category(scorecard, dice)`, which returns the name of the available category where these dice would score the most. If there's a tie, return the one that comes first in `CATEGORIES`. It must not change `scorecard` or `dice`. Then update `play_turn` so that typing `hint` at the category prompt prints the suggestion and asks again.

```python
card = new_scorecard()
print(best_category(card, [2, 5, 2, 5, 5]))   # full house
record(card, "full house", [2, 5, 2, 5, 5])
print(best_category(card, [2, 5, 2, 5, 5]))   # three of a kind
```

**B. A robot player.** Write `auto_game()`, which plays a whole game with no `input()` and returns the final score. Your robot needs a rerolling strategy: a simple one is "find the most common number and reroll every die that isn't showing it." Then use `best_category` to choose where to score. Run `auto_game()` 1000 times and print the average score. Can you change the strategy so the average goes up?

