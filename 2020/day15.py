from collections import defaultdict, deque


def compute(nums, end_turn):
    memory = defaultdict(lambda: deque([], maxlen=2))
    for turn, n in enumerate(nums, start=1):
        memory[n].append(turn)
    last_num = n
    for turn in range(turn+1, end_turn+1):
        last_seen = memory[last_num]
        if len(last_seen) == 1:
            last_num = 0
        else:
            last_num = last_seen[1] - last_seen[0]
        memory[last_num].append(turn)
    return last_num


if __name__ == '__main__':
    data = [int(x) for x in open("15.txt").read().split(",")]
    print("Part 1 answer: ", compute(data, 2020))
    print("For part 2 this is gonna take some time...")
    print("Part 2 answer: ", compute(data, 30000000))
