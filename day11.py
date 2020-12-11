from copy import deepcopy


def part1_2(stat, fill_below, empty_above, part2=False):
    next_stat = [['#' if pos == 'L' else '.' for pos in line]
                 for line in stat]

    while next_stat != stat:

        stat = next_stat

        next_stat = deepcopy(stat)
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                if stat[i][j] == '.':
                    continue

                adjs = 0
                for di, dj in deltas:
                    ai, aj = i + di, j + dj
                    if part2:
                        while stat[ai][aj] == '.' and \
                                0 < ai < height + 1 and \
                                0 < aj < width + 1:
                            ai += di
                            aj += dj

                    if stat[ai][aj] == '#':
                        adjs += 1

                if stat[i][j] == '#' and adjs >= empty_above:
                    next_stat[i][j] = 'L'
                elif stat[i][j] == 'L' and adjs <= fill_below:
                    next_stat[i][j] = '#'

    occupied = sum(line.count('#') for line in stat)
    return occupied


if __name__ == '__main__':
    with open('inputs/11.txt') as _file:
        start_stat = [list(line.strip()) for line in _file]

    height = len(start_stat)
    width = len(start_stat[0])

    deltas = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    start_stat = [
        ['.'] * (width + 2),
        *[['.'] + line + ['.'] for line in start_stat],
        ['.'] * (width + 2),
    ]
    print("Part 1 answer: ", part1_2(deepcopy(start_stat), 0, 4))
    print("Part 2 answer: ", part1_2(deepcopy(start_stat), 0, 5, part2=True))
