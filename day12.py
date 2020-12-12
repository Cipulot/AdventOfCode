def part_1(lines):
    # 0 = N
    # 1 = E
    # 2 = S
    # 3 = W
    bear = 1

    x = 0
    y = 0

    dX = {0: 0, 1: 1, 2: 0, 3: -1, "N": 0, "S": 0, "E": 1, "W": -1}
    dY = {0: 1, 1: 0, 2: -1, 3: 0, "N": 1, "S": -1, "E": 0, "W": 0}

    turn = {"L": -1, "R": 1}

    for line in lines:
        dir, val = line[0], int(line[1:])

        if dir in "LR":
            val /= 90
            bear = (bear + turn[dir]*val) % 4

        elif dir in "NSEW":
            x += dX[dir]*val
            y += dY[dir]*val

        elif dir == "F":
            x += dX[bear]*val
            y += dY[bear]*val

    return abs(x) + abs(y)


def part_2(lines):
    x = 0
    y = 0

    wx = 10
    wy = 1

    w_dX = {"N": 0, "S": 0, "E": 1, "W": -1}
    w_dY = {"N": 1, "S": -1, "E": 0, "W": 0}

    for line in lines:
        dir, val = line[0], int(line[1:])

        if dir in "NSEW":
            wx += w_dX[dir]*val
            wy += w_dY[dir]*val

        elif dir in "L":
            for _ in range(val // 90):
                wx, wy = -wy, wx

        elif dir == "R":
            for _ in range(val // 90):
                wx, wy = wy, -wx

        elif dir == "F":
            x += wx * val
            y += wy * val

    return abs(x) + abs(y)


if __name__ == '__main__':
    with open('12.txt') as _file:
        lines = [line for line in _file.read().splitlines()]

    print("Part 1 answer: ", part_1(lines))
    print("Part 2 answer: ", part_2(lines))
