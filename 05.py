from aoc import *
from collections import deque
import re

data = get_input(5)


def split_boxes(boxes: str):
    result = []
    for i in range(1, len(boxes) - 1, 4):
        result.append(boxes[i])
    return result


def parse_input() -> list[list[deque], list[list[int]]]:
    [boxes, moves] = data.split("\n\n")
    boxes_parsed = [split_boxes(line) for line in boxes.splitlines() if line[1] != "1"]
    moves_parsed = [
        list(map(int, re.findall("\d+", move))) for move in moves.splitlines()
    ]

    queues = [deque() for _ in boxes_parsed[0]]
    for box_line in boxes_parsed:
        for i in range(0, len(box_line)):
            if box_line[i] != " ":
                queues[i].appendleft(box_line[i])

    return [queues, moves_parsed]


def part1():
    [boxes, moves] = parse_input()

    for [num, f, t] in moves:
        for _ in range(0, num):
            boxes[t - 1].append(boxes[f - 1].pop())

    return "".join([q.pop() for q in boxes])


print("Part 1:", part1())


def part2():
    [boxes, moves] = parse_input()

    for [num, f, t] in moves:
        q = deque()
        for _ in range(0, num):
            q.appendleft(boxes[f - 1].pop())
        boxes[t - 1].extend(q)

    return "".join([q.pop() for q in boxes])


print("Part 2:", part2())
