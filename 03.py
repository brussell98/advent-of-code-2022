from aoc import *

data = get_input(3)

a = 97
A = 65


def part1():
    lines = [
        [line[: (len(line) // 2)], line[(len(line) // 2) :]]
        for line in data.splitlines()
    ]

    sameTypes = [set(line[0]).intersection(set(line[1])) for line in lines]

    sum = 0
    for types in sameTypes:
        type = types.pop()
        sum += (ord(type) - a + 1) if type.islower() else (ord(type) - A + 27)

    return sum


print("Part 1:", part1())


def part2():
    groups = chunk(data.splitlines(), 3)
    sum = 0
    for group in groups:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                sum += (ord(char) - a + 1) if char.islower() else (ord(char) - A + 27)
                break

    return sum


print("Part 2:", part2())
