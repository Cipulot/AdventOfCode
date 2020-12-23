def part_1(data):
    cups = [*map(int,list(data))]
    cc = 0

    for _ in range(100):
        c1,c2,c3 = cups[(cc + 1) % len(cups)] , cups[(cc + 2) % len(cups)] , cups[(cc + 3) % len(cups)]
        dc = cups[cc] - 1
        ccv = cups[cc]

        cups.remove(c1)
        cups.remove(c2)
        cups.remove(c3)

        while dc not in cups:
            dc = dc - 1 if dc > 1 else 9 

        cups.insert(cups.index(dc) + 1, c3)
        cups.insert(cups.index(dc) + 1, c2)
        cups.insert(cups.index(dc) + 1, c1)
        cc = ( cups.index(ccv) + 1 ) % len(cups)

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

    cc = cups[0]

    for i in range(10000000):
        c1 = ls[cc]
        c2 = ls[c1]
        c3 = ls[c2]

        ls[cc] = ls[c3]
        dc =  1000000 if cc == 1 else cc -1

        while dc in [c1,c2,c3]:
            dc = 1000000 if dc == 1 else dc - 1

        ls[c3] = ls[dc]
        ls[dc] = c1
        cc = ls[cc]

    return ls[1] * ls[ls[1]]

if __name__ == "__main__":
    data = open('23.txt','r').read()
    print("Part 1 answer: ", part_1(data))
    print("Part 2 answer: ", part_2(data))