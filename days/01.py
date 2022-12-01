from aoc import *

elves = [map(int, elf.splitlines()) for elf in data.split("\n\n")]
sums = [sum(elf) for elf in elves]
sums.sort(reverse=True)

print("Most Calories:", max(sums))
print("Top 3:", sum(sums[:3]))
