def part_1(data):
    p1, p2 = "\n".join(data).split("\n\n")
    p1, p2 = [int(c) for c in p1.split("\n")[1:]], [int(c) for c in p2.split("\n")[1:]]
    while p1 and p2:
        win, loser = (p1, p2)[p2[0] > p1[0]], (p1, p2)[p2[0] < p1[0]]
        win += [win.pop(0), loser.pop(0)]
    return sum((i + 1) * c for i, c in enumerate(reversed(p1 or p2)))

def part_2(data):
    p1, p2 = "\n".join(data).split("\n\n")
    p1, p2 = [int(c) for c in p1.split("\n")[1:]], [int(c) for c in p2.split("\n")[1:]]

    def run_game(p1, p2):
        decks_p1, decks_p2 = set(), set()
        while p1 and p2:
            deck1, deck2 = tuple(p1), tuple(p2)
            if deck1 in decks_p1 or deck2 in decks_p2:
                return 0
            decks_p1.add(deck1)
            decks_p2.add(deck2)
            if len(p1) > p1[0] and len(p2) > p2[0]:
                win_pos = run_game(p1[1:p1[0] + 1], p2[1:p2[0] + 1])
            else:
                win_pos = p2[0] > p1[0]
            win, loser = (p1, p2)[win_pos], (p1, p2)[not win_pos]
            win += [win.pop(0), loser.pop(0)]
        return [p1, p2].index(win)

    run_game(p1, p2)
    return sum((i + 1) * c for i, c in enumerate(reversed(p1 or p2)))

if __name__ == '__main__':
    with open('22.txt') as _file:
        data = [line for line in _file.read().splitlines()]

    print("Part 1 answer: ", part_1(data))
    print("Part 2 answer: ", part_2(data))