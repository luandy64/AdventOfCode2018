#!/usr/bin/env python3

import ipdb
points = []
sx = 100
lx = -1
sy = 100
ly = -1
with open('day10a.txt') as input_file:
    for line in input_file:
        bacon = line.strip().split()
        x = int(bacon[1][:-1])
        y = int(bacon[2][:-1])
        dx = int(bacon[4][:-1])
        dy = int(bacon[5][:-1])
        points.append(((y, x), (dx, dy)))

        if x < sx:
            sx = x
        elif x > lx:
            lx = x

        if y < sy:
            sy = y
        elif y > ly:
            ly = y


def move(jerky):
    old_point, velocity = jerky
    new_point = (old_point[0] + velocity[1], old_point[1] + velocity[0])
    return (new_point, velocity)


def display(points):
    coords = [x[0] for x in points]

    for i in range(sx, lx):
        for j in range(sy, ly):
            if (i, j) in coords:
                print('#', end='')
            else:
                print('.', end='')
        print('')


user = input('q to quit: ')
while user != 'q':
    display(points)

    points = list(map(move, points))

    user = input('q to quit: ')

print('Done!')
