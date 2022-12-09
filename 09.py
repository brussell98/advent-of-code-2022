from aoc import *

data = get_input(9, example=False)


def solve_for_length(length: int):
    moves = [line.split(" ") for line in data.splitlines()]
    visited = set()
    visited.add((0, 0))

    parts = [[0, 0] for _ in range(0, length)]

    for move in moves:
        dir = move[0]
        steps = int(move[1])

        head = parts[0]

        for _ in range(0, steps):
            if dir == "U":
                head[1] += 1
            elif dir == "D":
                head[1] -= 1
            elif dir == "R":
                head[0] += 1
            else:
                head[0] -= 1

            for i in range(1, length):
                move_tail(parts[i - 1], parts[i])

            tail = parts[-1]
            visited.add((tail[0], tail[1]))

    return len(visited)


def move_tail(head: tuple[int, int], tail: tuple[int, int]):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]

    if abs(x_diff) > 1:
        if x_diff > 0:
            tail[0] += 1
        else:
            tail[0] -= 1
        if y_diff != 0:
            if y_diff > 0:
                tail[1] += 1
            else:
                tail[1] -= 1
    elif abs(y_diff) > 1:
        if y_diff > 0:
            tail[1] += 1
        else:
            tail[1] -= 1
        if x_diff != 0:
            if x_diff > 0:
                tail[0] += 1
            else:
                tail[0] -= 1


def part1():
    return solve_for_length(2)


print("Part 1:", part1())


def part2():
    return solve_for_length(10)


print("Part 2:", part2())
