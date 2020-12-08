def exec(OP_code, code_changed=None):
    order = 1
    acc, ptr = 0, 0
    looked = [0 for line in OP_code]
    while not looked[ptr]:
        looked[ptr] = order
        order += 1

        op, arg = OP_code[ptr]

        if order == code_changed:
            op = "nop"

        if op == "acc":
            acc += int(arg)
            ptr += 1
        if op == "jmp":
            ptr += int(arg)
        if op == "nop":
            ptr += 1

        if ptr > len(OP_code) - 1:
            return True, acc

    return False, acc


def part2(OP_code):
    jmp_cmd_indexes = [i for i, c in enumerate(OP_code) if c[0] == "jmp"]

    #A little print to show the list of indexes
    #print(jmp_cmd_indexes)

    finished, i = False, 0
    while not finished:
        finished, acc = exec(OP_code, jmp_cmd_indexes[i]-1)
        i += 1

    return acc


if __name__ == "__main__":
    with open("8.txt") as _file:
        data = _file.read().strip()
        OP_code = [line.split(" ") for line in data.splitlines()]

        ___, acc = exec(OP_code)

        print("Part 1 answer: ", acc)
        print("Part 2 answer: ", part2(OP_code))
