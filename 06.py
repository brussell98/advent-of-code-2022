from aoc import *

data = get_input(6)


def part1():
    for i in range(4, len(data) - 1):
        part = data[(i - 4) : i]
        if len(part) == len(set(part)):
            return i


print("Part 1:", part1())


def part2():
    for i in range(14, len(data) - 1):
        part = data[(i - 14) : i]
        if len(part) == len(set(part)):
            return i


print("Part 2:", part2())
