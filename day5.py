#!/usr/bin/env python3

import re
import string

def reacts(pair):
    if len(pair) == 2:
        f, s = pair[0], pair[1]
        if f.lower() == s.lower():
            return pair in [f.lower() + s.upper(), f.upper() + s.lower()]
        else:
            return False
    else:
        return False


def fuse(polymer):
    triggered = True

    while(triggered):
        i = 0
        triggered = False
        while i < len(polymer) - 1 :
            pair = polymer[i:i+2]
            if reacts(pair):
                polymer = polymer[0:i]+polymer[i+2:]
                triggered = True
            else:
                i += 1
    return len(polymer)

def part1():
    polymer = ''
    with open('corey.txt') as input:
        polymer = input.read().strip()

    print(fuse(polymer))
    
def part2():
    polymer = ''
    with open('day5a.txt') as input:
        polymer = input.read().strip()

    lengths = []
    for letter in string.ascii_lowercase:
        drop_letter = polymer.replace(letter, '').replace(letter.upper(), '')
        lengths.append(fuse(drop_letter))

    print(min(lengths))

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
