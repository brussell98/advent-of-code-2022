from aoc import *

data = get_input(17, example=False)

shape1 = [[True, True, True, True]]
shape2 = [[False, True, False], [True, True, True], [False, True, False]]
shape3 = [[True, True, True], [False, False, True], [False, False, True]]
shape4 = [[True], [True], [True], [True]]
shape5 = [[True, True], [True, True]]
shapes = [shape1, shape2, shape3, shape4, shape5]
shape_pos = 0
shapes_len = len(shapes)

arrows = data.strip()
arrow_pos = 0
arrows_len = len(arrows)


def limit_x(x: int, piece_length):
    if x < 0:
        return 0
    if x > 6 - piece_length:
        return 6 - piece_length
    return x


def get_next_shape():
    global shape_pos
    global shapes_len
    if shape_pos >= shapes_len:
        shape_pos = 0

    shape_pos += 1
    return shapes[shape_pos - 1]


def get_next_arrow():
    global arrow_pos
    global arrows_len
    if arrow_pos >= arrows_len:
        arrow_pos = 0

    # print(arrows[arrow_pos])
    arrow_pos += 1
    return arrows[arrow_pos - 1]


def place_on_board(board: list[list[bool]], piece: list[list[bool]], pos: list[int]):
    height = len(piece) - 1
    # print("Placing at", pos)
    for i in range(0, len(piece)):
        for k in range(0, len(piece[0])):
            if piece[i][k] == True:
                board[pos[1] - height + i][pos[0] + k] = piece[i][k]


def play_piece(board: list[list[bool]]):
    piece = get_next_shape()
    piece_length = len(piece[0]) - 1

    for _ in range(0, len(piece)):
        board.append([False] * 7)

    pos = [2, len(board) - 1]
    for _ in range(0, 3):
        pos[0] = limit_x(pos[0] + (1 if get_next_arrow() == ">" else -1), piece_length)

    while True:
        # c = [line.copy() for line in board.copy()]
        # place_on_board(c, piece, pos)
        # print_board(c)
        arrow = get_next_arrow()
        new_x = limit_x(pos[0] + (1 if arrow == ">" else -1), piece_length)
        if not check_for_intersection(board, piece, [new_x, pos[1]]):
            pos[0] = new_x

        if check_for_intersection(board, piece, [pos[0], pos[1] - 1]):
            place_on_board(board, piece, pos)
            break

        pos[1] -= 1

    # Trim top rows
    i = len(board) - 1
    while i >= 0:
        if True not in board[i]:
            board.pop(i)
            i -= 1
        else:
            break


def check_for_intersection(
    board: list[list[bool]], piece: list[list[bool]], position: list[int]
):
    piece_height = len(piece)
    piece_width = len(piece[0])

    x = position[0]
    y = position[1]

    if y < 0:
        return True

    for i in range(0, piece_height):
        for k in range(0, piece_width):
            if board[i + (y - piece_height + 1)][k + x] == True and piece[i][k] == True:
                return True

    return False


def print_board(board: list[list[bool]]):
    cb = board.copy()
    cb.reverse()

    length = len(cb)

    for i in range(0, length):
        print(
            f"{(length - i - 1):3}", "".join(["#" if b == True else "." for b in cb[i]])
        )


def solve_for_iterations(iterations, part2=False):
    global shape_pos
    global arrow_pos
    shape_pos = 0
    arrow_pos = 0
    board = []
    change = []

    for i in range(0, iterations):
        length_before = len(board)
        play_piece(board)
        if part2:
            change.append(len(board) - length_before)
        # print(f"----------------- {i + 1}")
        # print_board(board)
        # print("-----------------")

    if part2:
        with open("17-changes.txt", "w") as file:
            file.write("\n".join(list(map(str, change))))

    return len(board)


def part1():
    return solve_for_iterations(2022)


print("Part 1:", part1())


def part2():
    # return solve_for_iterations(10000, True)

    iterations = 1000000000000
    front = []
    cycle = []
    with open("./input/17_front.txt", "r") as file:
        front = list(map(int, file.read().splitlines()))
    with open("./input/17_cycle.txt", "r") as file:
        cycle = list(map(int, file.read().splitlines()))

    iterations -= len(front)
    remaining = iterations % len(cycle)
    cycles = iterations // len(cycle)

    return sum(front) + cycles * sum(cycle) + sum(cycle[:remaining])


print("Part 2:", part2())
