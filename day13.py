import math

def part_1_2(data):
    t = int(data[0])
    B = [(i,int(b)) for i,b in enumerate(data[1].split(',')) if b != 'x']

    T = [(b, b-(t%b)) for _,b in B]

    print("Part 1 answer: ", math.prod(min(T, key=lambda x: x[1])))

    p,t = 1,0
    for dt,b in B:
        while True:
            if (dt+t) % b == 0: break
            t += p
        p *= b

    print("Part 2 answer: ", t)

if __name__ == '__main__':
    with open('13.txt') as _file:
        data = _file.readlines()

    part_1_2(data)