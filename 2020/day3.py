def count_trees(woods, step):
    pos = (0, 0)
    n_trees = 0

    while pos[1] < len(woods):
        if woods[pos[1]][pos[0] % len(woods[0])] == '#':
            n_trees += 1

        pos = (pos[0] + step[0], pos[1] + step[1])

    return n_trees

if __name__ == '__main__':
    with open("3.txt") as f:
        woods = []
        for row in f:
            woods.append(row.strip())

        print("Part 1 answer: ", count_trees(woods, (3, 1)))

        #TRIGGER WANRING: if you're using Python3.8 you could bypass all of the following by using the math.prod([count_trees(woods, x) for x in to_check]
        n_trees = 1
        to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        for x in to_check:
            n_trees *= count_trees(woods, x)
        print("Part 1 answer: ", n_trees)