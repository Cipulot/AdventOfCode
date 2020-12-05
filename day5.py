if __name__ == '__main__':
    with open('5.txt') as _file:

        _table = str.maketrans('BFRL', '1010')
        seats = _file.read().translate(_table).splitlines()
        ids = tuple(map(lambda s: int(s, 2), seats))

        id_min = min(ids)
        id_max = max(ids)

        expect = id_max * (id_max + 1) // 2 - id_min * (id_min - 1) // 2
        own_id = expect - sum(ids)

        print("Part 1 answer: ", max(ids))
        print("Part 2 answer: ", own_id)