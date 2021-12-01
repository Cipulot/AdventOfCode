import itertools
import copy
import time


def part_1(data):
    grid = [[['.' for _ in range(24)] for _ in range(24)] for _ in range(24)]
    for ix, i in enumerate(data):
        for jx, j in enumerate(i):
            grid[12][ix+9][jx+9] = j

    for _ in range(6):
        grid_copy = copy.deepcopy(grid)
        for i in range(24):
            for j in range(24):
                for k in range(24):
                    active_count = 0
                    for z in itertools.product([0, 1, -1], repeat=3):
                        if not(z == (0, 0, 0))\
                                and (0 <= i + z[0] <= 23) \
                                and (0 <= j + z[1] <= 23) \
                                and (0 <= k + z[2] <= 23) \
                                and grid[i+z[0]][j+z[1]][k+z[2]] == '#':
                            active_count += 1

                    if (grid[i][j][k] == '#') and (not(2 <= active_count <= 3)):
                        grid_copy[i][j][k] = '.'

                    if (grid[i][j][k] == '.') and (active_count == 3):
                        grid_copy[i][j][k] = '#'
        grid = grid_copy

    active = 0
    for i in range(24):
        for j in range(24):
            for k in range(24):
                if grid[i][j][k] == '#':
                    active += 1
    return active


def part_2(data):
    grid = [[[['.' for _ in range(24)] for _ in range(24)]
             for _ in range(24)] for _ in range(24)]
    for ix, i in enumerate(data):
        for jx, j in enumerate(i):
            grid[12][12][ix+9][jx+9] = j

    for _ in range(6):
        grid_copy = copy.deepcopy(grid)
        for i in range(24):
            for j in range(24):
                for k in range(24):
                    for l in range(24):
                        active_count = 0
                        for z in itertools.product([0, 1, -1], repeat=4):
                            if not(z == (0, 0, 0, 0))\
                                    and (0 <= i + z[0] <= 23) \
                                    and (0 <= j + z[1] <= 23) \
                                    and (0 <= k + z[2] <= 23) \
                                    and (0 <= l + z[3] <= 23) \
                                    and (grid[i+z[0]][j+z[1]][k+z[2]][l+z[3]] == '#'):
                                active_count += 1

                        if (grid[i][j][k][l] == '#') and not(2 <= active_count <= 3):
                            grid_copy[i][j][k][l] = '.'

                        if (grid[i][j][k][l] == '.') and (active_count == 3):
                            grid_copy[i][j][k][l] = '#'
        grid = grid_copy

    active = 0
    for i in range(24):
        for j in range(24):
            for k in range(24):
                for l in range(24):
                    if grid[i][j][k][l] == '#':
                        active += 1
    return active


if __name__ == '__main__':
    part_1_time = time.time()
    with open('inputs/17.txt') as _file:
        data = [line for line in _file.read().splitlines()]

    print("Part 1 answer: ", part_1(data))
    print("--- %s seconds for reading from file and executing part_1 ---" % (time.time() - part_1_time))
    part_2_time = time.time()
    print("For part 2 this is gonna take some time (I don't have time rn to optimize)...")
    print("Part 2 answer: ", part_2(data))
    print("--- %s seconds for executing part_2 ---" % (time.time() - part_2_time))
