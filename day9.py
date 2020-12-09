def get_first_invalid_num(input, pre_len):
    for index, num in enumerate(input):
        if index >= pre_len:
            check = False
            prev_input = input[index - pre_len: index]

            for ix, i in enumerate(prev_input):
                for jx, j in enumerate(prev_input):
                    if ix > jx:
                        if i + j == num:
                            check = True
            if not check:
                return num
    return -1


def get_set_to_target(input, tar):
    sum_of_set = 0
    left_index = 0
    right_index = 0

    # sliding window solution
    while left_index <= right_index < len(input):
        next_num = input[right_index]

        if sum_of_set + next_num < tar:
            sum_of_set += next_num
            right_index += 1

        elif sum_of_set + next_num == tar:
            return input[left_index: right_index + 1]

        else:
            while sum_of_set + next_num > tar:
                sum_of_set -= input[left_index]
                left_index += 1
    return []


def part1(input):
    return get_first_invalid_num(input, 25)


def part2(input):
    first_invalid_num = get_first_invalid_num(input, 25)
    continuous_set = get_set_to_target(input, first_invalid_num)
    return min(continuous_set) + max(continuous_set)


if __name__ == "__main__":
    with open('inputs/9.txt') as _file:
        input_from_file = [int(line) for line in _file.read().splitlines()]
        inputs = [int(item) for item in input_from_file]

        print("Part 1 answer: ", part1(inputs))
        print("Part 2 answer: ", part2(inputs))
