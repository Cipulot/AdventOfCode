import pyparsing as pp


def parse(expression):
    child_expressions = []
    for child_expr in expression:
        if isinstance(child_expr, pp.ParseResults):
            child_expressions.append(parse(child_expr))
        else:
            child_expressions.append(child_expr)
    while len(child_expressions) > 2:
        res = eval("".join(map(str, child_expressions[0:3])))
        child_expressions = [res] + child_expressions[3:]
    return int(child_expressions[0])


if __name__ == '__main__':
    with open('18.txt') as _file:
        lines = [line for line in _file.read().splitlines()]

    part_1_rule = pp.infixNotation(
        pp.Word(pp.nums), [(pp.oneOf("* / + -"), 2, pp.opAssoc.LEFT)])
    part_1 = [part_1_rule.parseString(line) for line in lines]

    part_2_rule = pp.infixNotation(pp.Word(pp.nums), [(
        pp.oneOf("+ -"), 2, pp.opAssoc.LEFT), (pp.oneOf("* /"), 2, pp.opAssoc.LEFT)])
    part_2 = [part_2_rule.parseString(line) for line in lines]

    print("Part 1 answer: ", sum(parse(expression) for expression in part_1))
    print("Part 2 answer: ", sum(parse(expression)for expression in part_2))
