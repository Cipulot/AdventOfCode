def part_1(inputs, set_of_inputs):
    for input in inputs:
        if 2020 - input in set_of_inputs:
            return input * (2020 - input)

def part_2(inputs, set_of_inputs):
    for input_0 in inputs:
        for input_1 in inputs:
            if (2020 - input_0 - input_1) in set_of_inputs:
                return input_0 * (2020 - input_0 - input_1) * input_1

if __name__ == '__main__':
    with open('1.txt') as _file:
        inputs = [int(line) for line in _file]
        set_of_inputs = set(inputs)
        print("Part 1 answer: ", part_1(inputs, set_of_inputs))
        print("Part 2 answer: ", part_2(inputs, set_of_inputs))
