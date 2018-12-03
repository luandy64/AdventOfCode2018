#!/usr/bin/env python3

def part1():
    two = 0
    three = 0
    with open('day2a.txt') as input:
        for line in input:
            count = {}
            for letter in line:
                if letter not in count:
                    count[letter] = 1
                else:
                    count[letter] += 1
            if 2 in count.values():
                two += 1

            if 3 in count.values():
                three += 1

    print(two, three, (two*three))


def part2():
    ids = []
    with open('day2a.txt') as input:
        for line in input:
            ids.append(line)

        for i in range(len(ids[0])):
            drop = [word[0:i] + word[i+1:] for word in ids]
            for j in range(len(drop)):
                if drop[j] in (drop[0:j] + drop[j+1:]):
                    print(drop[j])
                    return

def main():
    selection = int(input("Run (1) or (2): "))

    while(True):
        if selection == 1:
            part1()
            return
        elif selection == 2:
            part2()
            return
        else:
            selection = int(input("Run (1) or (2): "))


if __name__ == '__main__':
    main()

