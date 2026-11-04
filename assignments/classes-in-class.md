# CIS001 In-Class: A Card Class

Note: [These are the slides](https://ben-allen.github.io/CIS-001/slides/12-classes-and-objects-part-2.pdf) that go with this sheet. Each problem matches a "Your turn" slide.

## How to work through this

The slides build a `Die` class one method at a time. On this sheet you'll build a **`Card`** class (a playing card) the same way. Each problem uses the idea the slides just showed for `Die`, applied to `Card`. Keep the `Die` slides open: they're your model.

Many of these problems ask you to **predict first, then run**. Write your prediction down *before* you run the code. Getting a prediction wrong is fine, and it's how you'll learn the most today. When a prediction is wrong, take a moment to work out *why* before you move on.

If you get stuck, open the **Hint** under the problem. Try for a couple of minutes before you open it.

Work in one Colab notebook (or one `.py` file). You'll add a method to `Card` in each problem, so keep the whole class in one place, and put your test code **below** the class, not inside it.

## Problem 1: the `Card` class

A playing card has a **rank** and a **suit**. We'll use the numbers 1 to 13 for the rank (1 is an ace, 11 a jack, 12 a queen, 13 a king) and a string for the suit: `"hearts"`, `"diamonds"`, `"clubs"`, or `"spades"`.

**a)** Write a class `Card` with a docstring and an `__init__(self, rank, suit)` method that stores both values as attributes named `rank` and `suit`.

**b)** Add a method `color(self)` that returns `"red"` if the card's suit is hearts or diamonds, and `"black"` otherwise. Unlike `roll`, this method doesn't change the card. It returns an answer.

Test it:

```python
c = Card(12, "hearts")
print(c.rank, c.suit)               # should print 12 hearts
print(c.color())                    # should print red
print(Card(5, "spades").color())    # should print black
```

<details><summary>Hint</summary>
Look at <code>Die.__init__</code> on the slides: it has one parameter besides <code>self</code> and one line in its body. <code>Card.__init__</code> has two of each. For <code>color</code>, you can check <code>if self.suit in ("hearts", "diamonds"):</code>.
</details>

## Problem 2: `__str__` and `__repr__`

**a)** Before you change anything, predict what this prints. Then run it.

```python
c = Card(12, "hearts")
print(c)
```

**b)** Add these two methods to `Card`:

- `__str__` returns a string like `"12 of hearts"`.
- `__repr__` returns a string that looks like the code that would make the card: `"Card(12, 'hearts')"`.

Remember: both of them **return** a string. Neither one prints anything.

**c)** Predict each line, then run it:

```python
c = Card(12, "hearts")
print(c)
print([c, Card(1, "spades")])
print("you drew the " + str(c))
```

<details><summary>Hint</summary>
An f-string is the easiest way to build these: <code>f"{self.rank} of {self.suit}"</code>. In <code>__repr__</code>, the suit needs single quotes around it inside the string, so it looks like <code>'hearts'</code> and not like a variable named <code>hearts</code>. If you get <code>TypeError: __str__ returned non-string (type NoneType)</code>, your method printed the string instead of returning it.
</details>

## Problem 3: `__eq__`

**a)** Run this **before** you add `__eq__`. Predict each line first.

```python
a = Card(12, "hearts")
print(a == Card(12, "hearts"))
print(a == Card(12, "spades"))

pile = [Card(1, "clubs"), Card(5, "clubs")]
print(Card(5, "clubs") in pile)
```

**b)** In one sentence: why does `a == Card(12, "hearts")` give that answer, even though both cards are the queen of hearts?

**c)** Add `__eq__` to `Card`. Two cards are equal when the rank **and** the suit both match. Run the code from part (a) again. Which lines changed?

**d)** The last line didn't use `==`, but its answer changed anyway. What does that tell you about how `in` searches a list?

<details><summary>Hint</summary>
The <code>Die</code> version compares one attribute. Yours compares two, joined with <code>and</code>.
</details>

## Problem 4: `__lt__` and sorting

**a)** Add `__lt__` to `Card`. Compare **ranks only**: one card is less than another when its rank is smaller. Ignore the suits.

**b)** Predict each line, then run it:

```python
hand = [Card(12, "hearts"),
        Card(3, "spades"),
        Card(7, "clubs")]
print(sorted(hand))
print(max(hand))
print(Card(5, "hearts") < Card(5, "spades"))
print(Card(5, "spades") < Card(5, "hearts"))
```

**c)** Look at the last two lines. Neither card is less than the other, but with your `__eq__` they aren't equal either. Is that a problem for sorting a hand of cards? Why or why not?

<details><summary>Hint</summary>
For (b): <code>print(sorted(hand))</code> prints a list, so which dunder method shows the cards? <code>print(max(hand))</code> prints one card, so which one is used there?
</details>

## Problem 5: face cards

Change `__str__` so that aces and face cards print with their names: rank 1 prints as `A`, 11 as `J`, 12 as `Q`, and 13 as `K`. Every other rank prints as its number. Leave `__repr__` alone.

```python
print(Card(12, "hearts"))    # should print Q of hearts
print(Card(1, "spades"))     # should print A of spades
print(Card(7, "clubs"))      # should print 7 of clubs
print([Card(12, "hearts")])  # should print [Card(12, 'hearts')]
```

<details><summary>Hint</summary>
An <code>if</code>/<code>elif</code> chain works. So does a dictionary: <code>{1: "A", 11: "J", 12: "Q", 13: "K"}</code>. Use <code>in</code> to check whether the rank is one of its keys.
</details>
