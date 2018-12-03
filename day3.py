#!/usr/bin/env python3

import numpy as np

def parse_input(line):
    args = line.split()
    claim_id = int(args[0][1:])
    h, w = [int(num) for num in args[3].split('x')]
    start = dict( (x,y) for x,y  in zip(["row", "col"],[int(num) for num in args[2][:-1].split(',')]))
    return (claim_id, start, h, w)


def part1():
    fabric = np.zeros((1500,1500))
    with open('day3a.txt') as input:
        for line in input:
            claim_id, start, height, width = parse_input(line)

            for i in range(height):
                for j in range(width):
                    fabric[start['row'] + i][start['col'] + j] += 1

    count = 0
    for i in range(len(fabric)):
        for j in range(len(fabric[0])):
            if fabric[i][j] > 1:
                count += 1
    print(count)


def part2():

    fabric = np.zeros((1500,1500))
    duplicate = []
    canon = []

    with open('day3a.txt') as input:
        for line in input:
            claim_id, start, height, width = parse_input(line)
            canon.append(claim_id)

            for i in range(height):
                for j in range(width):
                    if fabric[start['row'] + i][start['col'] + j] != 0:
                        duplicate.append(int(fabric[start['row'] + i][start['col'] + j]))
                        duplicate.append(claim_id)

                    fabric[start['row'] + i][start['col'] + j] = claim_id
    print([x for x in canon if x not in duplicate])


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
