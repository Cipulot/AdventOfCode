from collections import defaultdict

coordinate_mapping = {'nw': (-1, 1), 'ne': (1, 1),
                      'sw': (-1, -1), 'se': (1, -1), 'e': (2, 0), 'w': (-2, 0)}


def part_1(data):
    tiles = defaultdict(lambda: True)
    tiles[(0, 0)] = True
    for line in data:
        line = list(line.strip())
        directions = []
        while len(line) > 0:
            val = line.pop(0)
            if val in ['s', 'n']:
                val += line.pop(0)
            directions.append(coordinate_mapping.get(val))
        x, y = 0, 0
        for direction in directions:
            x, y = x + direction[0], y + direction[1]
        tiles[(x, y)] = not tiles[(x, y)]

    b_tiles = set([loc for loc, white in tiles.items() if not white])
    return b_tiles, len(b_tiles)


def part_2(b_tiles_param):
    for _ in range(100):
        no_flips = set()
        w_neigh = defaultdict(int)
        for loc in b_tiles_param:
            b_neigh_cnt = 0
            for dir in coordinate_mapping.values():
                x, y = dir[0] + loc[0], dir[1] + loc[1]
                if (x, y) in b_tiles_param:
                    b_neigh_cnt += 1
                else:
                    w_neigh[(x, y)] += 1
            if 1 <= b_neigh_cnt <= 2:
                no_flips.add(loc)

        w_flips = set([loc for loc, count in w_neigh.items() if count == 2])
        b_tiles_param = set.union(w_flips, no_flips)

    return len(b_tiles_param)


if __name__ == '__main__':
    with open('inputs/24.txt') as _file:
        data = [line for line in _file.read().splitlines()]

    res_1 = part_1(data)
    res_2 = part_2(res_1[0])
    print("Part 1 answer: ", res_1[1])
    print("Part 2 answer: ", res_2)
