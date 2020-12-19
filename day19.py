def sequence_run(g, seq, s):
    if not seq:
        yield s
    else:
        k, *seq = seq
        for s in run(g, k, s):
            yield from sequence_run(g, seq, s)


def alt_run(g, alt, s):
    for seq in alt:
        yield from sequence_run(g, seq, s)


def run(g, k, s):
    if isinstance(g[k], list):
        yield from alt_run(g, g[k], s)
    else:
        if s and s[0] == g[k]:
            yield s[1:]


def match(g, s):
    return any(m == '' for m in run(g, '0', s))


if __name__ == '__main__':
    with open('19.txt') as _file:
        rulesdata, stringsdata = _file.read().split('\n\n')
    strings = stringsdata.split('\n')
    rules = {}
    for line in rulesdata.split('\n'):
        k, rule = line.split(': ')
        if rule[0] == '"':
            rule = rule[1:-1]
        else:
            rule = [seq.split(' ') if ' ' in seq else [seq]
                    for seq in (rule.split(' | ') if ' | ' in rule else [rule])]
        rules[k] = rule

    print("Part 1 answer: ", sum(match(rules, s) for s in strings))
    rules = {**rules, '8': [['42'], ['42', '8']],
             '11': [['42', '31'], ['42', '11', '31']]}
    print("Part 2 answer: ", sum(match(rules, s) for s in strings))
