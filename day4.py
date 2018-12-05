#!/usr/bin/env python3

from collections import defaultdict

def make_map():
    with open('day4a.txt') as input:
        d = defaultdict(list)
        curr_guard = ''
        for line in input:
            sigfigs = line.strip().split()
            time, guard_id = parse(sigfigs)
            if len(sigfigs) == 4:
                d[curr_guard].append(time)
            elif len(sigfigs) == 6:
                curr_guard = guard_id
            else:
              print('Unknown line encountered', line)
              exit()
    return d


def parse(line):
# if len(line) == 4, line[3] is garbage we don't use
# if len(line) == 6, line[1] is never used
    return (line[1][:-1], line[3])


def part1():
    d = make_map()

    e = defaultdict(list)
    for k,v in d.items():
        for i in range(1,len(v)+1,2):
            wake_time = int(v[i][-2:])
            start_time = int(int(v[i-1][-2:]))
            time_asleep =  wake_time - start_time
            e[k].append(time_asleep)

    f = [(x,sum(y)) for x,y in e.items()] #[(guard_id, total min asleep)]
    g = max(f,key=lambda x: x[1]) # (guard_id, total min asleep)

    minutes = d.get(g[0])
    h = dict((x,0) for x in range(60)) # {0:0, 1:0, 2:0 ... 59:0}
    for i in range(1,len(minutes)+1,2):
        start = minutes[i-1][-2:]
        end = minutes[i][-2:]
        for j in range(int(start),int(end)): # "build layers" of time asleep
            h[j] += 1

    last_most_minute = list(h.values())[::-1].index(max(h.values())) # the answer needed the last occurance of the max minute
    print(g[0], [thing[1][0] for thing in enumerate(h.items()) if thing[0] == (59 - last_most_minute)][0])
    # The above line is screaming for a list.index() I think


def part2():
    d = make_map()

    # START "build layers"
    e = {}
    for k in d.keys():
        e[k] = [0]*60

    for k,v in e.items():
        minutes = d.get(k)
        for i in range(1,len(minutes)+1,2):
            start = minutes[i-1][-2:]
            end = minutes[i][-2:]
            for j in range(int(start),int(end)):
                v[j] += 1
    # END "build layers"

    overall_max = set()

    # Add every number we see to the set named overall_max
    for k,v in e.items():
        for thing in v:
            overall_max.add(thing)

    the_max = max(overall_max) # the actual overall max

    # the_max happened to be unique, so find the key (the guard_id) and the minute associated with the_max
    for k,v in e.items():
        if the_max in v:
            print(k,v.index(the_max))
            break

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
