from aoc import *

data = get_input(4)


def part1():
    lines = [line.split(",") for line in data.splitlines()]
    parsedLines = [
        [
            list(map(int, line[0].split("-"))),
            list(map(int, line[1].split("-"))),
        ]
        for line in lines
    ]

    def is_overlap(line):
        one = line[0]
        two = line[1]
        return (
            True
            if (one[0] <= two[0] and one[1] >= two[1])
            or (two[0] <= one[0] and two[1] >= one[1])
            else False
        )

    overlapping = [line for line in parsedLines if is_overlap(line)]

    return len(overlapping)


print("Part 1:", part1())


def part2():
    lines = [line.split(",") for line in data.splitlines()]
    parsedLines = [
        [
            list(map(int, line[0].split("-"))),
            list(map(int, line[1].split("-"))),
        ]
        for line in lines
    ]

    def is_overlap(line):
        one = set(range(line[0][0], line[0][1] + 1))
        two = set(range(line[1][0], line[1][1] + 1))

        return len(one & two) > 0

    overlapping = [line for line in parsedLines if is_overlap(line)]

    return len(overlapping)


print("Part 2:", part2())
