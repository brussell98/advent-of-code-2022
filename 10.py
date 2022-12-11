from aoc import *

data = get_input(10, example=False)


def part1():
    lines = [line.split(" ") for line in data.splitlines()]
    cycles_to_record = [20, 60, 100, 140, 180, 220]
    pending_cycles = []
    x = 1
    strengths = []

    cycle = 1
    while cycle <= cycles_to_record[-1]:
        if cycle in cycles_to_record:
            strengths.append(x * cycle)

        if len(pending_cycles) != 0:
            pending_cycle = pending_cycles.pop(0)
            x += pending_cycle

            cycle += 1
            continue

        if len(lines) == 0:
            cycle += 1
            continue

        instruction = lines.pop(0)
        if instruction[0] == "addx":
            pending_cycles.append(int(instruction[1]))

        cycle += 1

    return strengths, sum(strengths)


print("Part 1:", part1())


def part2():
    lines = [line.split(" ") for line in data.splitlines()]
    pending_cycles = []
    x = 1

    screen = ["."] * (40 * 6)

    for cycle in range(0, len(screen)):
        pos = cycle % 40

        if abs(pos - x) < 2:
            screen[cycle] = "#"

        if len(pending_cycles) != 0:
            pending_cycle = pending_cycles.pop(0)
            x += pending_cycle

            continue

        if len(lines) == 0:
            continue

        instruction = lines.pop(0)
        if instruction[0] == "addx":
            pending_cycles.append(int(instruction[1]))

    return "\n".join(["".join(line) for line in chunk(screen, 40)])


print(f"Part 2:\n{part2()}")
