def bit_set(val: int, bit: int):
    return val | (1 << bit)


def clear_bit(val: int, bit: int):
    return val & ~(1 << bit)


def mask_on(mask_str: str, val: int) -> int:
    result = val
    for i, bit_val in enumerate(mask_str):
        ind_bit = len(mask_str)-1-i

        if bit_val == '0':
            result = clear_bit(result, ind_bit)
        elif bit_val == '1':
            result = bit_set(result, ind_bit)
    return result


def decode_addrs(mask_str: str, val: int, mem_addr: int) -> set:
    init_addr = mem_addr

    for i in range(len(mask_str)):
        if mask_str[len(mask_str)-1-i] == '1':
            init_addr = bit_set(init_addr, i)

    curr_addrs = set([init_addr])
    for i in range(len(mask_str)):
        if mask_str[len(mask_str)-1-i] == 'X':
            new_addrs = set()
            for addr in curr_addrs:
                new_addrs.add(bit_set(addr, i))
                new_addrs.add(clear_bit(addr, i))
            curr_addrs = curr_addrs.union(new_addrs)
    return curr_addrs


def result_giver(mem_dict_X: dict):
    partX_res = 0
    for mem_val in mem_dict_X.values():
        if mem_val != 0:
            partX_res += mem_val
    return partX_res


if __name__ == '__main__':
    mask_str = ''
    mem_dict_1 = {}
    mem_dict_2 = {}
    with open('14.txt') as fp:
        line = fp.readline()
        while line:
            tokens = line.strip().split()
            if line.startswith('mask'):
                mask_str = tokens[2]
            else:
                mem_addr, val = int(tokens[0][4:-1]), int(tokens[2])

                # Part 1 dict
                mem_dict_1[mem_addr] = mask_on(mask_str, val)

                # Part 2 dict
                for addr in decode_addrs(mask_str, val, mem_addr):
                    mem_dict_2[addr] = val
            line = fp.readline()

    print("Part 1 answer: ", result_giver(mem_dict_1))
    print("Part 2 answer: ", result_giver(mem_dict_2))
