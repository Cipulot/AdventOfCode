from collections import defaultdict
import functools
import operator
import math
import re


def ext(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]


def rotate(g):
    xs = []
    for i in range(len(g)):
        s = ''.join(x[i] for x in g)
        xs.append(s)

    return tuple(reversed(xs))


def flip(g):
    return tuple(reversed(g))


def left_edge(g):
    return ''.join(x[0] for x in g)


def right_edge(g):
    return ''.join(x[-1] for x in g)


def edges(g):
    return [g[0], g[-1], left_edge(g), right_edge(g)]


def all_edges(g):
    es = edges(g)
    return es + [''.join(reversed(x)) for x in es]


def moves(g):
    for _ in range(4):
        yield g
        yield flip(g)
        g = rotate(g)


MONSTER = """\
                  #
#    ##    ##    ###
 #  #  #  #  #  #   """.split('\n')


def main():
    with open('20.txt') as _file:
        data = [x.strip().split('\n')
                for x in _file.read().strip().split('\n\n')]

    tiles = {}
    for tile in data:
        n = ext(tile[0])[0]
        tiles[n] = flip(tile[1:])

    N = int(math.sqrt(len(tiles)))

    edge_map = defaultdict(list)
    for n, tile in tiles.items():
        for e in all_edges(tile):
            edge_map[e].append(n)

    corners = []
    for n, tile in tiles.items():
        count = 0
        for e in edges(tile):
            count += len(edge_map[e]) - 1
        if count == 2:
            corners.append(n)

    corner_n = corners[0]
    l_tile = tiles[corner_n]
    while len(edge_map[left_edge(l_tile)]) == 2:
        l_tile = rotate(l_tile)

    def pick(ln, l_grid):
        re = right_edge(l_grid)
        me = [x for x in edge_map[re] if x != ln][0]
        m_tile = tiles[me]
        for m_tile in moves(m_tile):
            if re == left_edge(m_tile):
                break
        return me, m_tile

    m_grid = [[None] * N for x in range(N)]
    m_grid[0][0] = corner_n, l_tile
    for y in range(0, N):
        if y > 0:
            ln, l_grid = m_grid[y-1][0]
            me, m_tile = pick(ln, flip(rotate(l_grid)))
            m_grid[y][0] = (me, flip(rotate(m_tile)))

        for x in range(1, N):
            ln, l_grid = m_grid[y][x-1]
            m_grid[y][x] = pick(ln, l_grid)

    n_grid = [[None] * N for x in range(N)]
    for i, row in enumerate(m_grid):
        for j, (_, col) in enumerate(row):
            x = list(col[1:-1])
            for k in range(len(x)):
                x[k] = x[k][1:-1]
            n_grid[i][j] = x

    pic = []
    for i, row in enumerate(n_grid):
        for i2 in range(len(row[0])):
            s = ''
            for j, col in enumerate(n_grid[i]):
                s += col[i2]
            pic.append(s)

    for pic in moves(pic):
        count = 0
        for y in range(len(pic)-len(MONSTER)):
            for x in range(len(pic)-len(MONSTER[0])):
                match = True
                for y0 in range(len(MONSTER)):
                    for x0 in range(len(MONSTER[y0])):
                        if MONSTER[y0][x0] == '#' and pic[y+y0][x+x0] != '#':
                            match = False
                            break
                    if not match:
                        break

                if match:
                    count += 1

        if count:
            break

    part1 = functools.reduce(operator.mul, corners)
    print("Part 1 answer: ", part1)

    everything = ''.join(pic).count('#')
    monster = ''.join(MONSTER).count('#')
    print("Part 2 answer: ", everything - monster * count)


if __name__ == '__main__':
    main()
