def check_count_in_range(password, letter, start, stop):
    return password.count(letter) >= start and password.count(letter) <= stop


def check_indexes(password, letter, start, stop):
    return (password[start] == letter or password[stop] == letter) and (password[start] != password[stop])

if __name__ == '__main__':
    counter_part1 = 0
    counter_part2 = 0
    with open('2.txt') as _file:
        letters = [input.split(": ") for input in _file]

        for policy, password in letters:
            length, letter = policy.split(" ")
            start, stop = length.split("-")
            start, stop = int(start), int(stop)

            if check_count_in_range(password, letter, start, stop): counter_part1 += 1
            if check_indexes(password, letter, start - 1, stop - 1): counter_part2 += 1

    print("Part 1 answer: ", counter_part1)
    print("Part 2 answer: ", counter_part2)