def part_1(groups_list):
    return sum([len(set("".join(g))) for g in groups_list])

def part_2(groups_list):
    result = 0
    for group in groups_list:
        for i, answers in enumerate(group):
            current = set(answers) if i == 0 else current.intersection(set(answers))
        result += len(current)
    return result

if __name__ == "__main__":
    with open("6.txt", 'r') as _file:
        input = _file.read()
        groups = input.split('\n\n')
        groups_list = [[answers for answers in group.split("\n")] for group in groups]

    print("Part 1 answer: ", part_1(groups_list))
    print("Part 2 answer: ", part_2(groups_list))