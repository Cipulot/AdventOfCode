def part_1(min_range, max_range):
    invalid = 0

    for line in lines[25:]:
        fields = [int(x) for x in line.split(',')]
        for field in fields:
            if field not in range(min_range, max_range + 1):
                invalid += field

    return invalid


def part_2(min_range, max_range):
    valid = []

    for line in lines[25:]:
        fields = [int(x) for x in line.split(',')]
        if all([field in range(min_range, max_range + 1) for field in fields]):
            valid.append(fields)

    possible = {}

    for col in range(len(valid[0])):
        possible_rules = []

        fields = [valid[i][col] for i in range(len(valid))]
        for rule, criteria in rules.items():
            if check_rule(criteria, fields):
                possible_rules.append(rule)
        possible[col] = possible_rules

    ordered_pairs = sorted([(len(val), key) for key, val in possible.items()])
    ordered_cols = [x[1] for x in ordered_pairs]

    confirmed_fields = {}
    for col in ordered_cols:
        possible_rules = possible[col]
        for field in confirmed_fields.keys():
            possible_rules.remove(field)
        confirmed_fields[possible_rules[0]] = col

    ticket = [int(x) for x in lines[22].split(',')]
    prod = 1
    for key, value in confirmed_fields.items():
        if key.startswith('departure'):
            prod *= ticket[value]

    return prod


def check_rule(rule, fields):
    first_crit = range(rule[0][0], rule[0][1] + 1)
    second_crit = range(rule[1][0], rule[1][1] + 1)
    return all([field in first_crit or field in second_crit for field in fields])


if __name__ == '__main__':
    with open('16.txt', 'r') as _file:
        lines = [x.rstrip() for x in _file.readlines()]

    rules = {}
    for rule in lines[:20]:
        field_name = rule.split(': ')[0]
        first_crit = rule.split(': ')[1].split(' or ')[0]
        range_one_min = int(first_crit.split('-')[0])
        range_one_max = int(first_crit.split('-')[1])
        second_crit = rule.split(': ')[1].split(' or ')[1]
        range_two_min = int(second_crit.split('-')[0])
        range_two_max = int(second_crit.split('-')[1])
        rules[field_name] = [(range_one_min, range_one_max),
                             (range_two_min, range_two_max)]

    min_range = min(crit[0] for rule in rules.values() for crit in rule)
    max_range = max(crit[1] for rule in rules.values() for crit in rule)

    print("Part 1 answer: ", part_1(min_range, max_range))
    print("Part 2 answer: ", part_2(min_range, max_range))
