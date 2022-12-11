from aoc import *
import re
import numpy

data = get_input(11, example=False)


def part1():
    monkeys = [lines.splitlines() for lines in data.split("\n\n")]

    monkey_inspections = [0] * len(monkeys)

    monkey_items = []
    for monkey in monkeys:
        monkey_items.append(list(map(int, re.findall(r"\d+", monkey[1]))))

    for round in range(0, 20):
        for i in range(0, len(monkeys)):
            monkey = monkeys[i]
            for _ in range(0, len(monkey_items[i])):
                monkey_inspections[i] += 1
                item = monkey_items[i].pop(0)
                op = re.findall(r"\*|\+|\d+|old$", monkey[2])
                if op[0] == "*":
                    if op[1] == "old":
                        item *= item
                    else:
                        item *= int(op[1])
                elif op[0] == "+":
                    if op[1] == "old":
                        item += item
                    else:
                        item += int(op[1])
                item //= 3

                test = re.search(r"\d+", monkey[3])
                if item % int(test.group()) == 0:
                    target = int(re.search(r"\d+", monkey[4]).group())
                    monkey_items[target].append(item)
                else:
                    target = int(re.search(r"\d+", monkey[5]).group())
                    monkey_items[target].append(item)

    monkey_inspections.sort(reverse=True)

    return monkey_inspections[0] * monkey_inspections[1]


print("Part 1:", part1())


def part2():
    monkeys = [lines.splitlines() for lines in data.split("\n\n")]

    monkey_inspections = [0] * len(monkeys)

    monkey_items = []
    monkey_ops = []
    monkey_test = []
    monkey_target = []
    for monkey in monkeys:
        monkey_items.append(list(map(int, re.findall(r"\d+", monkey[1]))))
        monkey_ops.append(re.findall(r"\*|\+|\d+|old$", monkey[2]))
        monkey_test.append(int(re.search(r"\d+", monkey[3]).group()))
        monkey_target.append(
            [
                int(re.search(r"\d+", monkey[4]).group()),
                int(re.search(r"\d+", monkey[5]).group()),
            ]
        )

    lcm = int(numpy.lcm.reduce(monkey_test))

    for round in range(0, 10000):
        for i in range(0, len(monkeys)):
            monkey = monkeys[i]
            for _ in range(0, len(monkey_items[i])):
                monkey_inspections[i] += 1
                item = monkey_items[i].pop(0)
                op = monkey_ops[i]

                if op[0] == "*":
                    if op[1] == "old":
                        item *= item
                    else:
                        item *= int(op[1])
                elif op[0] == "+":
                    if op[1] == "old":
                        item += item
                    else:
                        item += int(op[1])

                item %= lcm

                test = monkey_test[i]
                targets = monkey_target[i]
                if item % test == 0:
                    monkey_items[targets[0]].append(item)
                else:
                    monkey_items[targets[1]].append(item)

    monkey_inspections.sort(reverse=True)

    return monkey_inspections[0] * monkey_inspections[1]


print("Part 2:", part2())
