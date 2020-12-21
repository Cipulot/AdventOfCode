from functools import reduce
import re


def allergens(input):
    ingredient_list = []
    map_of_allergen = {}

    for line in input:
        m = re.match("^([\w\s]+) \(contains ([\w\s,]+)\)$", line).groups()

        ingredients = m[0].split(" ")
        allergens = m[1].split(", ")

        for allergen in allergens:
            if allergen not in map_of_allergen:
                map_of_allergen[allergen] = set(ingredients)
            else:
                map_of_allergen[allergen] &= set(ingredients)

        ingredient_list.extend(ingredients)

    safe_ingredients = set(ingredient_list) - reduce(lambda a,
                                                     b: a.union(b), map_of_allergen.values())
    result_1 = sum([ingredient_list.count(i) for i in safe_ingredients])

    unique_map_of_allergen = {}
    while max([len(v) for v in map_of_allergen.values()]) > 0:
        for k, v in map_of_allergen.items():
            if len(v) == 1:
                unique_map_of_allergen[k] = v.pop()
        for k in map_of_allergen:
            map_of_allergen[k] -= set(unique_map_of_allergen.values())

    result_2 = ','.join([v for k, v in
                         sorted([(k, v) for k, v in
                                 unique_map_of_allergen.items()])])

    return result_1, result_2


if __name__ == '__main__':
    with open("21.txt") as _file:
        results = allergens(_file)
    print("Part 1 answer: ", results[0])
    print("Part 2 answer: ", results[1])
