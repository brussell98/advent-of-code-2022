# Modified from: https://github.com/p7g/advent-of-code/blob/2021/aoc.py

from pathlib import Path
import requests
from collections import deque

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


def flatten(array):
    a = []
    for i in array:
        if isinstance(i, list):
            a.append(flatten(i))
        else:
            a.append(i)

    return a


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
            # Commented out for directed
            # self.vertices[v2].add(v1)

    def add_vertices_and_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)

        self.add_edge(v1, v2)

    def shortest_path(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return []

        # Use a queue to store the vertices we want to visit
        queue = deque([start])

        # Keep track of the previous vertex for each vertex, so we can
        # reconstruct the path when we reach the end
        prev = {start: None}

        while queue:
            vertex = queue.popleft()

            # Stop searching when we reach the end
            if vertex == end:
                break

            # Add all the neighbors of this vertex to the queue
            for neighbor in self.vertices[vertex]:
                if neighbor not in prev:
                    prev[neighbor] = vertex
                    queue.append(neighbor)

        # At this point, either we reached the end and `prev` contains the
        # shortest path, or there is no path and `prev` is empty
        if prev:
            # Reconstruct the shortest path
            path = [end]
            cur = end
            while cur != start:
                cur = prev[cur]
                path.append(cur)

            # Reverse the path and return it
            path.reverse()
            return path

        # If we didn't reach the end, there is no path
        return []
