from aoc import *

data = get_input(2)

hands = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
handValues = {"Rock": 1, "Paper": 2, "Scissors": 3}
results = {
    ("Rock", "Scissors"): 0,
    ("Paper", "Rock"): 0,
    ("Scissors", "Paper"): 0,
    ("Rock", "Rock"): 3,
    ("Paper", "Paper"): 3,
    ("Scissors", "Scissors"): 3,
    ("Rock", "Paper"): 6,
    ("Paper", "Scissors"): 6,
    ("Scissors", "Rock"): 6,
}

plays = [play.split(" ") for play in data.splitlines()]

score = 0
for play in plays:
    opponent = hands[play[0]]
    you = hands[play[1]]

    score += handValues[you] + results[(opponent, you)]

print("Total score:", score)

# Part 2
moves = {"X": 0, "Y": 3, "Z": 6}
neededPlayForResult = {
    ("Rock", 0): "Scissors",
    ("Paper", 0): "Rock",
    ("Scissors", 0): "Paper",
    ("Rock", 3): "Rock",
    ("Paper", 3): "Paper",
    ("Scissors", 3): "Scissors",
    ("Rock", 6): "Paper",
    ("Paper", 6): "Scissors",
    ("Scissors", 6): "Rock",
}

scoreCorrected = 0
for play in plays:
    opponent = hands[play[0]]
    outcome = moves[play[1]]

    you = neededPlayForResult[(opponent, outcome)]

    scoreCorrected += handValues[you] + outcome

print("Total score (corrected):", scoreCorrected)
