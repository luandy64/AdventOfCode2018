#!/usr/bin/env python3

def part1():
    total = 0
    with open('day1a.txt') as input:
        for line in input:
            total += int(line)

    print(total)

def part2():
    cache = [0]
    total = 0
    found = False
    while(not found):
        with open('day1a.txt') as input:
            for line in input:
                total += int(line)

                if total in cache:
                    print(total)
                    found = True
                    break
                else:
                    cache.append(total)




def main():
    call = int(input("Run (1) or (2): "))

    while(True):
        if call == 1:
            part1()
            return
        elif call == 2:
            part2()
            return
        else:
            call = int(input("Run (1) or (2): "))


if __name__ == '__main__':
    main()
