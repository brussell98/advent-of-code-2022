from aoc import *

increased = 0

lines = [int(line) for line in data.splitlines()]
for i in range(1, len(lines)):
    if lines[i] > lines[i - 1]:
        increased += 1

print(increased)
