from aoc import *

data = get_input(8, example=False)


def part1():
    lines = data.splitlines()
    flat = flatten(lines)

    count = 0

    for i in range(0, len(lines)):
        line = lines[i]
        if i == 0 or i == len(lines) - 1:
            count += len(line)
            continue

        for k in range(0, len(line)):
            value = line[k]
            if k == 0 or k == len(line) - 1:
                count += 1
                continue
            arrayOffset = i * len(lines)

            left = max(flat[arrayOffset : (arrayOffset + k)])
            right = max(flat[(arrayOffset + k + 1) : (arrayOffset + len(line))])

            top = max(flat[k : (k + arrayOffset) : len(line)])
            bottom = max(flat[(k + arrayOffset + len(line)) :: len(line)])

            if value > left or value > right or value > top or value > bottom:
                count += 1
                continue

    return count


print("Part 1:", part1())


def part2():
    lines = data.splitlines()
    flat = flatten(lines)

    best = 0

    for i in range(0, len(lines)):
        line = lines[i]
        for k in range(0, len(line)):
            value = line[k]
            leftScore = 0
            rightScore = 0
            topScore = 0
            bottomScore = 0
            arrayOffset = i * len(lines)

            left = reversed(flat[arrayOffset : (arrayOffset + k)]) if k != 0 else []
            right = (
                flat[(arrayOffset + k + 1) : (arrayOffset + len(line))]
                if k != len(line)
                else []
            )

            top = reversed(flat[k : (k + arrayOffset) : len(line)]) if i != 0 else []
            bottom = (
                flat[(k + arrayOffset + len(line)) :: len(line)]
                if i != len(lines)
                else []
            )

            for tree in left:
                if tree < value:
                    leftScore += 1
                if tree >= value:
                    leftScore += 1
                    break

            for tree in right:
                if tree < value:
                    rightScore += 1
                if tree >= value:
                    rightScore += 1
                    break

            for tree in top:
                if tree < value:
                    topScore += 1
                if tree >= value:
                    topScore += 1
                    break

            for tree in bottom:
                if tree < value:
                    bottomScore += 1
                if tree >= value:
                    bottomScore += 1
                    break

            score = leftScore * rightScore * topScore * bottomScore
            if score > best:
                best = score

    return best


print("Part 2:", part2())
