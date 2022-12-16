from aoc import *
import re

data = get_input(16, example=True)


def parse_input():
    valves = []
    for line in data.splitlines():
        name, rate, *paths = re.findall(
            r"[A-Z]{2}|\d+",
            line,
        )
        rate = int(rate)
        valves.append((name, rate, paths))

    return valves


def build_graph(valves):
    g = Graph()
    for valve in valves:
        name = valve[0]
        for path in valve[2]:
            g.add_vertices_and_edge(valve[0], path)

    return g


def build_distances(valves, graph: Graph):
    distances = {}
    for valve in valves:
        name = valve[0]
        distances[name] = {}
        for dest in valves:
            dest_name = dest[0]
            if dest_name == name:
                continue
            distances[name][dest_name] = len(graph.shortest_path(name, dest_name)) - 1

    return distances


# Doesn't work. No look-ahead
def part1():
    valves = parse_input()
    graph = build_graph(valves)

    distances = build_distances(valves, graph)
    print(distances)

    location = next((v for v in valves if v[0] == "AA"))
    open_valves = []
    flows = []
    pressure = 0
    minute = 0
    while minute < 30:
        pressure += sum(flows)
        dist = distances[location[0]]
        possible = [
            valve
            for valve in valves
            if valve[0] != location[0] and valve[1] != 0 and valve[0] not in open_valves
        ]
        if len(possible) == 0:
            minute += 1
            continue

        best = [None, 0]
        for valve in possible:
            value = valve[1] * (30 - minute - 1 - dist[valve[0]])
            if value > best[1]:
                best = [valve, value]

        current_value = (
            location[1] * (30 - minute - 1) if location[0] not in open_valves else 0
        )
        if current_value >= best[1]:
            open_valves.append(location[0])
            flows.append(location[1])
            minute += 1
            continue

        for _ in range(0, dist[best[0][0]]):
            pressure += sum(flows)
            dist = distances[location[0]]
            minute += 1
            if minute >= 30:
                break

        open_valves.append(best[0][0])
        flows.append(best[0][1])
        location = best[0]
        minute += 1

    print("minute", minute)
    print("flows", flows)
    print("open", open_valves)
    return pressure


print("Part 1:", part1())


def part2():
    pass


print("Part 2:", part2())
