from aoc import *

data = get_input(12, example=False)


def parse_pos(pos: str):
    if pos == "S":
        return ord("a") - 97
    elif pos == "E":
        return ord("z") - 97
    else:
        return ord(pos) - 97


def parse_input():
    array = [list(map(parse_pos, line)) for line in data.splitlines()]
    s_pos = data.index("S")
    e_pos = data.index("E")

    d = len(array[0]) + 1

    return (
        array,
        (s_pos // d, s_pos % d),
        (e_pos // d, e_pos % d),
    )


def to_graph(input):
    graph = Graph()

    for i in range(0, len(input)):
        for k in range(0, len(input[i])):
            graph.add_vertex((i, k))

            curr = input[i][k]
            top = input[i - 1][k] if i != 0 else None
            bottom = input[i + 1][k] if i != len(input) - 1 else None
            left = input[i][k - 1] if k != 0 else None
            right = input[i][k + 1] if k != len(input[i]) - 1 else None

            if top != None and top - curr <= 1:
                graph.add_vertices_and_edge((i, k), (i - 1, k))
            if bottom != None and bottom - curr <= 1:
                graph.add_vertices_and_edge((i, k), (i + 1, k))
            if left != None and left - curr <= 1:
                graph.add_vertices_and_edge((i, k), (i, k - 1))
            if right != None and right - curr <= 1:
                graph.add_vertices_and_edge((i, k), (i, k + 1))

    return graph


def part1():
    input, s_pos, e_pos = parse_input()
    print(s_pos, e_pos)
    graph = to_graph(input)

    path = graph.shortest_path(s_pos, e_pos)
    return len(path) - 1


print("Part 1:", part1())


def part2():
    input, s_pos, e_pos = parse_input()
    print(s_pos, e_pos)
    graph = to_graph(input)

    best_path = []
    for i in range(0, len(input)):
        # for k in range(0, len(input[0])):
        if input[i][0] == 0:
            try:
                path = graph.shortest_path((i, 0), e_pos)
                if len(best_path) == 0 or len(best_path) > len(path):
                    best_path = path
            except:
                continue

    return len(best_path) - 1


print("Part 2:", part2())
