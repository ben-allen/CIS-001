# Homework: Busy Beavers

Use our Turing machine: <https://ben-allen.github.io/CIS-001/tools/turing-machine.html>

Every machine in this homework starts on a **blank tape** (all 0s) in state 1. Write your machines the same way as last time: one line per state, the rule for reading 0 first, then the rule for reading 1. For example, the first machine we looked at in class is:

```
1: 1R2 1L2
2: 1L1 1L0
```

A busy beaver is a machine that leaves as many 1s as it can on a blank tape, using a fixed number of states, and then halts. Machines that run forever don't count, no matter how many 1s they write.

## Problem 1: one state

Write a machine that uses only state 1 (plus state 0 to halt). Fill in both cells. It must halt. How many 1s can it leave on the tape?

Then answer in one or two sentences: does the rule for reading 1 ever get used? Why or why not?

## Problem 2: halt or run forever?

Here are four machines:

```
# Machine A
1: 1R2 1L1
2: 1L1 1R0

# Machine B
1: 1R1 1L0
2: 1L1 1L1

# Machine C
1: 1R2 0R2
2: 1L1 0L1

# Machine D
1: 1R2 1L0
2: 1L1 1R2
```

For each machine, guess first: does it halt or run forever? Then check in the simulator.

- For each machine that halts, write how many 1s it leaves and how many steps it takes.
- For each machine that runs forever, explain how you know it will **never** halt. Running it for a long time doesn't prove it. Look at what it does over and over.

## Problem 3: the most 1s with two states

Write a machine that uses states 1 and 2 (plus state 0 to halt), fills all four cells, and halts. Make it leave as many 1s as you can.

Our first machine left four. If you can't beat it, give a different machine that ties it. Then explain in two or three sentences why you think no two-state machine can leave more.

## Problem 4: the longest run with two states

Same rules as Problem 3, but this time count **steps**, not 1s. Write a two-state machine that halts and takes as many steps as you can.

**Check it:** the simulator's message tells you how many steps the machine took before it halted.

Does your answer to this problem leave the most 1s too? Answer in one sentence.

## Problem 5: trace a three-state machine

Here is a three-state machine:

```
1: 1R2 1L0
2: 1L2 1L3
3: 1L1 1R3
```

Run it **by hand** on a blank tape. Write one row per step, like the whole run we did in class:

| step | state | reads | rule | tape after the step |
|---|---|---|---|---|
| 1 | 1 | 0 | 1R2 | ... |

Then check your table with the simulator. How many 1s does it leave? How many steps does it take? In one or two sentences, what is state 3's job?

## Problem 6: the most 1s with three states

Write a three-state machine (states 1, 2 and 3, plus state 0 to halt) that fills all six cells, halts, and leaves as many 1s as you can. Fill in this table and turn it in as text:

| state | reads 0 | reads 1 |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

Problem 5's machine leaves five 1s. You can do better.



## Turning it in

Turn in one text file with:

- your name
- your machines for each problem, written as text
- your answers to the questions in problems 1 through 6
- your table for problem 5
