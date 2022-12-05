# Modified from: https://github.com/p7g/advent-of-code/blob/2021/aoc.py

from pathlib import Path
import requests

__all__ = ["get_input", "chunk"]


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


def _get_input_path(day: int) -> str:
    return str(Path(__file__).parent / "input" / f"{day:02}.txt")


def get_input(day: int):
    try:
        with open(_get_input_path(day), "r") as f:
            return f.read()
    except FileNotFoundError:
        pass

    input_data = _fetch_input(day)
    _cache_input(day, input_data)
    return input_data
