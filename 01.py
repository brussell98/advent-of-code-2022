from aoc import *

data = get_input(1)

elves = [map(int, elf.splitlines()) for elf in data.split("\n\n")]
sums = [sum(elf) for elf in elves]
sums.sort(reverse=True)

print("Most Calories:", max(sums))
print("Top 3:", sum(sums[:3]))
