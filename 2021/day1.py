def read_file(file):
    with open(file, "r") as f:
        inp = [int(l.strip()) for l in f.readlines()]
    return inp


def part1(file, debug=False):
    inp = read_file(file)

    increased = 0
    for i in range(len(inp)):
        if debug:
            if i == 0:
                print("%i (N/A - no previous measurement)" % (inp[i]))

        if i > 0:
            if inp[i] > inp[i-1]:
                increased += 1
                if debug:
                    print("%i (increased)" % (inp[i]))
            if debug:
                if inp[i] < inp[i-1]:
                    print("%i (decreased)" % (inp[i]))
    return increased


def part2(file, debug=False):
    inp = read_file(file)

    increased = 0

    for i in range(len(inp)):
        if debug:
            if i == 2:
                print("%i (N/A - no previous measurement)" %
                      (inp[i]+inp[i-1]+inp[i-2]))
        if i > 2:
            previous = inp[i-1]+inp[i-2]+inp[i-3]
            current = inp[i]+inp[i-1]+inp[i-2]
            if current > previous:
                increased += 1
                if debug:
                    print("%i (increased)" % (current))
            if debug:
                if previous < current:
                    print("%i (decreased)" % (current))
    return increased


print("Part 1: %s measurements are larger than the previous measurement" %
      part1("input.txt"))
print("Part 2: %s measurements are larger than the previous measurement" %
      part2("input.txt"))
