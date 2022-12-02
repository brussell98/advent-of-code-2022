# Credit: https://github.com/p7g/advent-of-code/blob/2021/aoc.py

import datetime as dt
import sys
from pathlib import Path
import typing as t

data: str

__all__ = ["data"]


def __getattr__(name: str) -> t.Any:
    if name == "data":
        return _fetch_input()
    else:
        raise AttributeError(name)


def _main() -> None:
    date = _get_challenge_date()
    script_path = _get_challenge_script_path(date)
    with open(script_path, "r") as f:
        script_src = f.read()

    code = compile(source=script_src, filename=script_path, mode="exec")
    exec(code, {}, {})


def _get_challenge_date() -> dt.date:
    today = dt.datetime.today() + dt.timedelta(hours=1)

    day = int(sys.argv[1] if len(sys.argv) >= 2 else today.day)
    year = int(today.year)

    return dt.date(year=year, month=12, day=day)


def _get_challenge_script_path(date: dt.date) -> str:
    return str(Path(__file__).parent / "days" / f"{date.day:02}.py")


def _fetch_input():
    date = _get_challenge_date()
    input_path = _get_challenge_input_path(date)
    with open(input_path, "r") as f:
        return f.read().strip()


def _get_challenge_input_path(date: dt.date) -> str:
    return str(Path(__file__).parent / "input" / f"{date.day:02}.txt")


if __name__ == "__main__":
    _main()
