from aoc import *
import ast
from functools import cmp_to_key

data = get_input(13, example=False)


def test_list(left, right, booleans=False):
    len_left = len(left) - 1
    len_right = len(right) - 1

    for i in range(0, max(len(left), len(right))):
        if len_left < i:  # If left ended first
            return True if booleans else -1
        if len_right < i:  # If right ended first
            return False if booleans else 1

        l = left[i]
        r = right[i]

        if isinstance(l, list) or isinstance(r, list):
            nested_result = test_list(
                l if isinstance(l, list) else [l],
                r if isinstance(r, list) else [r],
                booleans,
            )
            if (booleans and nested_result != None) or (
                not booleans and nested_result != 0
            ):
                return nested_result
        else:
            if l < r:
                return True if booleans else -1
            if l > r:
                return False if booleans else 1

    return None if booleans else 0


def part1():
    groups = [
        list(map(ast.literal_eval, group.splitlines())) for group in data.split("\n\n")
    ]
    results = [test_list(group[0], group[1], True) for group in groups]

    sums = 0
    for i in range(0, len(groups)):
        if results[i] == True:
            sums += i + 1

    return sums


print("Part 1:", part1())


def part2():
    packets = [ast.literal_eval(line) for line in data.splitlines() if line != ""]
    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=cmp_to_key(test_list))

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


print("Part 2:", part2())
