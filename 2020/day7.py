import re
from collections import defaultdict


def color_search(c, all_colors, contained_by):
    for color in contained_by[c]:
        all_colors[color] = True
        if color in contained_by:
            color_search(color, all_colors, contained_by)


def sum_search(c, contains):
    return sum([x[0] * (sum_search(x[1], contains) + 1) if x[1] in contains else x[0] for x in contains[c]])


if __name__ == "__main__":
    contained_by = defaultdict(list)
    contains = defaultdict(list)

    with open("7.txt") as f:
        for line in f:
            s = line.split("contain")
            p1 = re.match(r'([a-z ]+) bags', s[0]).groups()[0]
            parts = re.findall(r'(\d+) ([a-z ]+) [bag|bags,. ]+', s[1])
            for bag in parts:
                contained_by[bag[1]].append(p1)
                contains[p1].append((int(bag[0]), bag[1]))

    contains_shiny_gold = {}
    color_search("shiny gold", contains_shiny_gold, contained_by)

    print("Part 1 answer: ", len(contains_shiny_gold.keys()))
    print("Part 2 answer: ", sum_search("shiny gold", contains))
