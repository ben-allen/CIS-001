import random


class Die:
    """One six-sided die."""

    def __init__(self, value):          # runs when you write Die(3)
        self.value = value

    def roll(self):
        self.value = random.randint(1, 6)

    def __str__(self):                  # print(d), str(d), f"{d}"
        return f"[{self.value}]"

    def __repr__(self):                 # print(dice) for a list of dice
        return f"Die({self.value})"

    def __eq__(self, other):            # a == b, a != b, in
        return self.value == other.value

    def __lt__(self, other):            # a < b, sorted, min, max
        return self.value < other.value


if __name__ == "__main__":
    d = Die(4)
    print(d)                            # [4]
    d.roll()
    print(d)                            # random: [1] to [6]

    dice = [Die(5), Die(2), Die(6)]
    print(dice)                         # [Die(5), Die(2), Die(6)]
    print(sorted(dice))                 # [Die(2), Die(5), Die(6)]
    print(max(dice))                    # [6]
    print(Die(4) == Die(4))             # True
