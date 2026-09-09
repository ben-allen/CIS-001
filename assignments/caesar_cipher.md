# Assignment: Secret Messages with the Caesar Cipher

## due 9/16

## Background

A **Caesar cipher** is one of the oldest encryption tricks around (Julius Caesar
supposedly used it to send military orders). The idea is simple: shift every
letter in a message forward by some fixed number of positions in the
alphabet.

For example, with a shift of `3`:

```
A -> D
B -> E
C -> F
...
X -> A
Y -> B
Z -> C
```

So the word `"CAT"` becomes `"FDW"`.

To decode a message, you just shift backwards by the same amount. This
assignment asks you to build an encoder, a decoder, and a way to crack a coded
message *without* knowing the shift.

This is the same shape as `bottle_verse` from the short assignment: you'll
write a small helper function that handles *one* piece (one letter), and a
bigger function that calls the helper repeatedly to handle the *whole* thing (a
full message). If you get stuck on the big function, it's usually because the
helper isn't quite right yet — test the helper by itself first.

---

## New tools you'll need

Everything else in this assignment builds on stuff you already know
(functions, `for` loops, `if`/`elif`/`else`, `%`). But there are three new
tools worth trying out *before* you start Part A, since the whole assignment
leans on them.

**1. `ord()` — turn a letter into a number**

Every character has a numeric code behind the scenes. `ord()` tells you
that code:

```python
print(ord('a'))   # 97
print(ord('b'))   # 98
print(ord('A'))   # 65
```

Notice `'a'` and `'A'` have *different* codes — that's the whole reason
you'll need to handle uppercase and lowercase separately.

**2. `chr()` — turn a number back into a letter**

`chr()` is the reverse of `ord()`:

```python
print(chr(97))   # a
print(chr(98))   # b
```

So `ord` and `chr` are inverses: `chr(ord('a'))` just gives you `'a'` back.
The trick to shifting a letter is: convert it to a number with `ord`, do
some arithmetic on the number, then convert back with `chr`.

**3. String indexing — grab one character out of a string**

You can pull out a single character from a string using square brackets and
a position number, starting from `0`:

```python
word = 'python'
print(word[0])   # p
print(word[1])   # y
print(word[5])   # n
```

Combined with `%` (which you already know), this lets you cycle through a
short string repeatedly no matter how far `i` goes:

```python
keyword = 'key'
for i in range(7):
    print(keyword[i % len(keyword)])
```

```
k
e
y
k
e
y
k
```

Try running both of these snippets yourself and poking at them a bit before
moving on — Part A and the Vigenère option both depend directly on this
pattern.

---

## Part A: Shifting a single letter

Write a function:

```python
def shift_letter(letter, shift):
    ...
```

that takes a single character and a shift amount, and returns the shifted
letter.

**Requirements:**
- Handle both uppercase and lowercase letters correctly (`shift_letter('a', 3)` should give `'d'`, not `'D'`).
- Wrap around the alphabet: `shift_letter('z', 1)` should give `'a'`, not `'{'`.
- If the input isn't a letter (like a space, comma, or digit), return it unchanged. Don't try to shift punctuation.

**Hints:**
- `ord(letter)` gives you the letter's numeric code; `chr(number)` turns a number back into a letter.
- `ord('a')` is a useful anchor point. Everything you need can be built from `ord(letter) - ord('a')`, some modular arithmetic (`% 26`), and adding `ord('a')` back.
- `letter.isupper()` and `letter.islower()` will help you handle both cases.

**Test it with:**
```python
print(shift_letter('a', 3))   # d
print(shift_letter('z', 1))   # a
print(shift_letter('Z', 1))   # A
print(shift_letter('!', 5))   # !
```

---

## Part B: Shifting a whole message

Now write:

```python
def caesar_encode(message, shift):
    ...
```

that takes a full string and returns the shifted version, using
`shift_letter` on each character in a loop. (Just like `bottle_verse` called
a helper function once per line, `caesar_encode` should call `shift_letter`
once per character.)

**Test it with:**
```python
print(caesar_encode("Meet me at midnight", 3))
```

Expected output:
```
Phhw ph dw plgqljkw
```

Then write `caesar_decode(message, shift)`. Think about how decoding relates
to encoding — it should be a very short function (one line calling
`caesar_encode` cleverly, or a near-copy with one small change).

**Test it with:**
```python
secret = caesar_encode("Meet me at midnight", 3)
print(caesar_decode(secret, 3))   # should give back the original message
```

---

## Part C: Crack it (no shift given!)

Here's a message someone sent you, encoded with an *unknown* shift:


```
"Bmjs Rw. Gnqgt Gfllnsx tk Gfl Jsi fsstzshji ymfy mj btzqi xmtwyqd gj hjqjgwfynsl mnx jqjajsyd-knwxy gnwymifd bnym f ufwyd tk xujhnfq rflsnknhjshj, ymjwj bfx rzhm yfqp fsi jchnyjrjsy ns Mtggnyts."
```

Write code that tries **all 26 possible shifts** and prints each result,
so you can read through them and spot the one that's actual English.

**Hint:** a `for` loop over `range(26)`, calling `caesar_decode` with each
value, printing the shift number alongside the result so you know which one
worked.

Once you find the real message, write it down as a comment in your code
along with the shift that revealed it.

---

## Part D (optional stretch)

1. **Vigenère cipher.** Instead of one fixed shift for the whole message, use
   a keyword where *each letter of the keyword* gives a different shift, and
   cycle through the keyword letter-by-letter as you go through the message:

   ```
   message:  H  E  L  L  O
   keyword:  K  E  Y  K  E
   shift:    10 4  24 10 4
   ```

   You'll still use `shift_letter` unchanged — the only new idea is looping
   through the message with an index `i`, and using `keyword[i % len(keyword)]`
   to pick which keyword letter (and therefore which shift) applies to
   position `i`. The `%` wraps you back to the start of the keyword once
   you run past its length.

---

## What to submit

A single `.py` file containing:
- `shift_letter`
- `caesar_encode`
- `caesar_decode`
- Your code for Part C, with a comment showing the decoded message and the shift that worked
- (Optional) anything you did from Part D


## Rough rubric (25 pts)

| Piece | Points |
|---|---|
| `shift_letter` handles upper/lower/non-letters correctly | 7 |
| `caesar_encode` works on full messages | 7 |
| `caesar_decode` works (and is short / reuses encode logic) | 5 |
| Part C: all 26 shifts tried, correct message identified | 6 |
| Part D | +5 bonus |
