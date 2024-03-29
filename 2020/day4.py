class Checker:
    def __init__(self, passport):
        self.passport = passport

    def check_field_count(self):
        return len(self.passport) == 8 or (len(self.passport) == 7 and 'cid' not in self.passport)

    def check_year(self, key, start, end):
        return len(self.passport[key]) == 4 and int(self.passport[key]) >= start and int(self.passport[key]) <= end

    def check_byr(self):
        return self.check_year('byr', 1920, 2002)

    def check_iyr(self):
        return self.check_year('iyr', 2010, 2020)

    def check_eyr(self):
        return self.check_year('eyr', 2020, 2030)

    def check_hcl(self):
        return self.passport['hcl'][0] == "#" and self.passport['hcl'][1:].isalnum()

    def check_ecl(self):
        return self.passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def check_pid(self):
        return len(self.passport['pid']) == 9

    def check_hgt(self):
        if self.passport['hgt'][-2:] == "cm":
            return int(self.passport['hgt'][:-2]) >= 150 and int(self.passport['hgt'][:-2]) <= 193
        elif self.passport['hgt'][-2:] == "in":
            return int(self.passport['hgt'][:-2]) >= 59 and int(self.passport['hgt'][:-2]) <= 76

    def is_valid(self):
        return (self.check_field_count() and self.check_byr() and self.check_iyr() and self.check_eyr()
                and self.check_hcl() and self.check_ecl() and self.check_pid() and self.check_hgt())


def get_passports(_file):
    passports = []
    passport = {}
    for line in _file:
        if line != "\n":
            line = line.rstrip().split(" ")
            line = [field.split(":") for field in line]
            for field in line:
                passport[field[0]] = field[1]
        else:
            passports.append(passport)
            passport = {}
    passports.append(passport)
    return passports


if __name__ == '__main__':
    counter_part1 = 0
    counter_part2 = 0

    with open('4.txt') as _file:
        passports = get_passports(_file)
        checkers = [Checker(passport) for passport in passports]

        for checker in checkers:
            if checker.check_field_count():
                counter_part1 += 1
            if checker.is_valid():
                counter_part2 += 1

    print("Part 1 answer: ", counter_part1)
    print("Part 2 answer: ", counter_part2)
