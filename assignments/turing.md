# Homework: Turing Machines

**Due:** 11/18

Use our Turing machine: <https://ben-allen.github.io/CIS-022/tools/turing-machine.html>

Numbers are written the way we wrote them in class: that many 1s in a row, with the head on the leftmost 1. For example, the number 4 is:

```
0 [1] 1 1 1 0 0 0
```


## Writing a machine down

To turn in a machine, type its rule table as text, one line per state. Use `-` for a blank cell. For example, the first machine we looked at in class is:

```
1: 1R2 1L2
2: 1L1 1L0
```

The first rule on each line is for reading 0. The second is for reading 1.

## Problem 1: subtract 2

Write a machine that takes away two 1s. It should work for any number that's 2 or more, and finish with the head on the leftmost 1.

**Check it:** starting with 3 on the tape, the message should end with "The tape holds 1, a well-formed number." Starting with 2, it should say the tape is blank.

## Problem 2: what does this machine do?

Type in this machine:

```
1: 1L2 0R1
2: 1L3 -
3: 0R0 -
```

Before you run it, guess what it does. Then run it starting with 2 on the tape, and again starting with 4. What does it do? Explain how it works in two or three sentences.

## Problem 3: add 1 on the other end

In class, Add 1 put the new 1 on the left end of the number. Write a machine that puts the new 1 on the **right** end instead. The head still has to finish on the leftmost 1.

So the leftmost 1 shouldn't move: if you start with the head on square 0, it should finish on square 0.

**Check it:** starting with 3, the message should end with "The tape holds 4, a well-formed number", and the head should be on the same square it started on.

Hint: this machine has to walk to the right end of the number and then walk back.

## Problem 4: double it, then add 1

Here is a machine that doubles a number:

```
1: 0R0 0R2
2: 0R3 1R2
3: 1R4 1R3
4: 1L5 -
5: 0L6 1L5
6: 0R1 1L6
```

Build a machine that computes 2x + 1 by joining this machine to your Add 1 machine from class:

1. Renumber your Add 1 machine's states so they come after the doubler's (7, 8, and so on).
2. Find the doubler's rule that halts. Change it so that instead of going to state 0, it goes to the first state of your Add 1 machine.

**Check it:** starting with 0, 1, 2 and 3 on the tape, the message should end with "The tape holds 1", "holds 3", "holds 5" and "holds 7".

## Problem 5: subtraction

Write a machine that subtracts one number from another. The tape starts with the first number, one 0, then the second number. The head starts on the leftmost 1. For 4 − 2:

```
0 [1] 1 1 1 0 1 1 0
```

When it halts, the tape should hold the answer as a well-formed number. You can assume the first number is at least as big as the second.

**Check it:**

| Start | The message should end with |
|---|---|
| 3 − 1 | The tape holds 2, a well-formed number. |
| 4 − 2 | The tape holds 2, a well-formed number. |
| 5 − 2 | The tape holds 3, a well-formed number. |
| 2 − 2 | The tape is blank. |

If you're stuck: describe a plan in plain English first. One plan that works is to erase one 1 from each number, over and over, until the second number is gone. Then write one state for each step of your plan. Problem 3's walk to the right end and back will come in handy.

## Problem 6: the second number is bigger

Run your subtraction machine on 2 − 3. What happens? Explain why in two or three sentences.

## Turning it in

Turn in one text file with:

- your name
- your machines for problems 1, 3, 4 and 5, written as text
- your answers to problems 2 and 6
