# CIS001 In-Class: A Deck of Cards

Today you'll build a `Deck` class that holds 52 `Card` objects.

## A note

The earlier sheets told you what to write, one step at a time. This one tells you what your `Deck` has to **do**, without providing starter code.

Some things to know:

- **You've seen everything you need**, with one or two small exceptions. Each exception has a hint.
- **Hints are hidden under each part.** Try for a few minutes before you open one. Being stuck for a little while is normal; that's where learning happens.
- **Test as you go.** Don't write the whole class and then run it. Write one method, try it, then move on.
- **Use these exact names:** `Deck`, `cards`, `shuffle`, and `deal`. This makes it possible for me to test your code.

## Getting started

Start from your `Card` class (problems 1–5 from last time). Put `Deck` in the same file or notebook, **below** `Card`.

## Part 1: the `Deck` class

### 1. A new deck

`Deck()` makes a deck with 52 cards: one card for each rank from 1 to 13, in each of the four suits. Keep the cards in a list, in an attribute named `cards`. A new deck should be in order: all the clubs first (ace up to king), then diamonds, then hearts, then spades.

```python
deck = Deck()
print(deck.cards[0])     # A of clubs
print(deck.cards[-1])    # K of spades
```

<details><summary>Hint</summary>
You need every suit paired with every rank. One loop inside another does that. A list of the four suits, in order, will be useful again in Part 2.
</details>

### 2. How many cards are left

`len(deck)` gives the number of cards in the deck. Right now it doesn't work:

```text
TypeError: object of type 'Deck' has no len()
```

Teach Python what `len` means for a deck, the same way you taught `print` what to do with a card.

<details><summary>Hint</summary>
<code>len(x)</code> calls a dunder method on <code>x</code>, the same way <code>print(x)</code> calls <code>__str__</code>. Its name follows the same pattern as the others: <code>__len__</code>. It takes only <code>self</code> and returns an int.
</details>

### 3. Printing a deck

`print(deck)` should show something useful instead of `<__main__.Deck object at 0x...>`. You decide what it looks like, but it should at least say how many cards are left, for example `Deck of 52 cards`. (Printing all 52 cards is allowed, but it's a lot.)

### 4. Shuffling

`deck.shuffle()` puts the cards in a random order. It changes the deck and returns nothing.

<details><summary>Hint</summary>
Python's <code>random</code> module has a function that shuffles a list in place: <code>random.shuffle(some_list)</code>. Remember to <code>import random</code> at the top of your file.
</details>

### 5. Dealing

`deck.deal(n)` takes `n` cards off the top of the deck and returns them as a list. The cards it deals are **gone** from the deck: after dealing 5 from a full deck, `len(deck)` is 47. Which end of the list counts as the "top" is up to you.

<details><summary>Hint</summary>
A list method you've used before both removes an item <em>and</em> gives it back to you.
</details>

### 6. Running out

If you ask for more cards than are left, `deal` gives you all the cards that are left, so `deck.deal(100)` on a full deck returns all 52 and leaves the deck empty.

### Check Part 1

When Part 1 works, this should run, and every line marked `# must be` should match:

```python
deck = Deck()
print(len(deck))          # must be 52
print(deck)               # your choice, e.g. Deck of 52 cards
print(deck.cards[0])      # must be A of clubs

deck.shuffle()
hand = deck.deal(5)
print(hand)               # 5 random cards
print(len(hand))          # must be 5
print(len(deck))          # must be 47
print(hand[0] in deck.cards)   # must be False: dealt cards are gone
```

## Part 2: a better `<`

Back in problem 4, your `__lt__` only compared ranks. So `Card(5, "hearts") < Card(5, "spades")` and `Card(5, "spades") < Card(5, "hearts")` were both `False`, even though the two cards aren't equal.

Change `__lt__` so that when two cards have the same rank, the suit breaks the tie, in this order: clubs < diamonds < hearts < spades. Lower ranks still come first.

```python
print(Card(5, "hearts") < Card(5, "spades"))   # True
print(Card(5, "spades") < Card(5, "hearts"))   # False
print(Card(4, "spades") < Card(5, "clubs"))    # True: rank still comes first
print(sorted([Card(5, "spades"), Card(2, "clubs"), Card(5, "hearts"), Card(5, "clubs")]))
# [Card(2, 'clubs'), Card(5, 'clubs'), Card(5, 'hearts'), Card(5, 'spades')]
```

<details><summary>Hint</summary>
Two ideas you've seen before work well together here. <code>index</code> tells you where an item is in a list, so it can turn a suit into a number. And Python compares tuples one item at a time, from the left.
</details>

## Part 3: high card

Write a function (not a method) called `high_card_game()` that:

- makes a new deck and shuffles it,
- deals 5 cards to each of two players,
- prints each player's hand, sorted,
- prints which player's highest card is higher, and what that card is.

It might print something like:

```text
Player 1: [Card(3, 'diamonds'), Card(7, 'clubs'), Card(7, 'diamonds'), Card(8, 'spades'), Card(13, 'diamonds')]
Player 2: [Card(2, 'clubs'), Card(5, 'clubs'), Card(5, 'hearts'), Card(6, 'clubs'), Card(10, 'clubs')]
Player 1 wins with K of diamonds
```

## Questions

Answer these in comments at the bottom of your file.

1. With the old, rank-only `__lt__`, could `high_card_game` ever have a tie for the highest card? Can it now? Why?
2. `high_card_game` is a function, but `deal` is a method. In a sentence or two, why does each one belong where it is?
