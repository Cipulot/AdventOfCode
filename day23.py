def part_1(data):
    cups = [*map(int,list(data))]
    current_cup = 0

    for _ in range(100):
        cup_1,cup_2,cup_3 = cups[(current_cup + 1) % len(cups)] , cups[(current_cup + 2) % len(cups)] , cups[(current_cup + 3) % len(cups)]
        dc = cups[current_cup] - 1
        current_cup_v = cups[current_cup]

        cups.remove(cup_1)
        cups.remove(cup_2)
        cups.remove(cup_3)

        while dc not in cups:
            dc = dc - 1 if dc > 1 else 9

        cups.insert(cups.index(dc) + 1, cup_1)
        cups.insert(cups.index(dc) + 1, cup_2)
        cups.insert(cups.index(dc) + 1, cup_3)

        current_cup = ( cups.index(current_cup_v) + 1 ) % len(cups)

    cups = cups[cups.index(1) + 1:] + cups[ :cups.index(1) ]
    return ''.join(map(str,cups))

def part_2(data):
    cups = [*map(int,list(data))]
    ls = {}

    for i in range(1000000):
        if i < len(cups) - 1:
            ls[cups[i]] = cups[i + 1]
        elif i == len(cups) - 1 :
            ls[cups[-1]] = max(cups) + 1
        else :
            ls[i + 1] = (i + 2)

    ls[1000000] = cups[0]

    current_cup = cups[0]

    for i in range(10000000):
        cup_1 = ls[current_cup]
        cup_2 = ls[cup_1]
        cup_3 = ls[cup_2]

        ls[current_cup] = ls[cup_3]
        dc =  1000000 if current_cup == 1 else current_cup -1

        while dc in [cup_1,cup_2,cup_3]:
            dc = 1000000 if dc == 1 else dc - 1

        ls[cup_3] = ls[dc]
        ls[dc] = cup_1
        current_cup = ls[current_cup]

    return ls[1] * ls[ls[1]]

if __name__ == "__main__":
    data = open('23.txt','r').read()
    print("Part 1 answer: ", part_1(data))
    print("Part 2 answer: ", part_2(data))