from aoc import *

data = get_input(7, example=False)


def get_dir(fs: dict, dir: str):
    result = fs

    for d in dir.split("/"):
        if d == "":
            continue
        result = result[d]

    return result


def parse_input(input):
    fs = dict()
    dir = ""
    for i in range(0, len(input)):
        line = input[i].split(" ")
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    dir = ""
                elif line[2] == "..":
                    dir = "/".join(dir.split("/")[:-1])
                else:
                    dir += "/" + line[2]
                continue
            elif line[1] == "ls":
                continue

        wd = get_dir(fs, dir)
        if line[0] == "dir":
            if line[1] not in wd:
                wd[line[1]] = dict()
            continue

        wd[line[1]] = int(line[0])

    return fs


def get_dir_size(dir: dict, name: str):
    sizes = []

    size = 0
    for key in dir.keys():
        if type(dir[key]) is dict:
            res = get_dir_size(dir[key], key)
            size += res[-1][1]
            sizes.extend(res)
        else:
            size += dir[key]

    sizes.append([name, size])
    return sizes


def part1():
    fs = parse_input(data.splitlines())

    dir_sizes = get_dir_size(fs, "/")

    return sum([size for _, size in dir_sizes if size <= 100000])


print("Part 1:", part1())


def part2():
    fs = parse_input(data.splitlines())

    dir_sizes = get_dir_size(fs, "/")
    needed = dir_sizes[-1][1] - 40000000
    dir_sizes.sort(key=lambda x: x[1])

    return next((size for _, size in dir_sizes if size >= needed))


print("Part 2:", part2())
