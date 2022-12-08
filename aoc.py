# Modified from: https://github.com/p7g/advent-of-code/blob/2021/aoc.py

from pathlib import Path
import requests

__all__ = ["get_input", "chunk", "flatten", "Graph"]


def chunk(arr: list, size: int):
    return [arr[i : i + size] for i in range(0, len(arr), size)]


def _read_session() -> str:
    with open(".aoc-session", "r") as f:
        return f.read().strip()


def _fetch_input(day: int) -> str:
    req = requests.get(
        f"https://adventofcode.com/2022/day/{day}/input",
        cookies={"session": _read_session()},
    )
    req.raise_for_status()
    return req.content.decode("ascii")


def _cache_input(day: int, aoc_input: str) -> None:
    with open(_get_input_path(day), "w") as f:
        f.write(aoc_input)


def _get_input_path(day: int, example=False) -> str:
    return str(
        Path(__file__).parent
        / "input"
        / f"{day:02}{'' if not example else '_example'}.txt"
    )


def get_input(day: int, example=False):
    try:
        with open(_get_input_path(day, example), "r") as f:
            return f.read()
    except FileNotFoundError:
        if example:
            raise Exception("No example input file")
        pass

    input_data = _fetch_input(day)
    _cache_input(day, input_data)
    return input_data


def flatten(array: list):
    flat_list = []
    for sublist in array:
        for item in sublist:
            flat_list.append(item)

    return flat_list


# ChatGPT
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)

    def add_vertices_and_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)

        self.add_edge(v1, v2)

    def distance(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            # One or both vertices are not in the graph
            return float("inf")

        # Use a breadth-first search to find the distance between the vertices
        visited = set()
        queue = [(v1, 0)]
        while queue:
            curr_vertex, curr_distance = queue.pop(0)
            if curr_vertex == v2:
                # We have reached the second vertex, so we can return the distance
                return curr_distance
            visited.add(curr_vertex)
            for neighbor in self.vertices[curr_vertex]:
                if neighbor not in visited:
                    # Add the neighbor to the queue to be visited
                    queue.append((neighbor, curr_distance + 1))

        # If we reach here, then there is no path between the two vertices
        return float("inf")
