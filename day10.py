def part1(nums):
    jolt_1 = 0
    jolt_3 = 0
    base = 0
    for i in range(len(nums)):
        jolt = min([x for x in nums if base < x <= (base + 3)])
        if (jolt - base) == 1:
            jolt_1 += 1
        if (jolt - base) == 3:
            jolt_3 += 1
        base = jolt

    return jolt_1 * (jolt_3 + 1)


def dist_ways_ways(nums, base, index, inf):
    if base == max(nums):
        return 1

    key = base * 10000 + index
    if key in inf:
        return inf[key]

    w = 0
    ad = [x for x in nums if base < x <= (base + 3)]
    for a in ad:
        if a in nums:
            w = w + dist_ways_ways(nums, a, index + 1, inf)

    inf[key] = w
    return w


def part2(nums):
    inf = {}
    return dist_ways_ways(nums, 0, 0, inf)


if __name__ == '__main__':
    with open('10.txt') as _file:
        lines = [int(line) for line in _file.read().splitlines()]
    nums = [int(x) for x in lines]

    print("Part 1 answer: ", part1(nums))
    print("Part 2 answer: ", part2(nums))
