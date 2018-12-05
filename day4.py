#!/usr/bin/env python3

from collections import defaultdict

def parse(line):
    log_line = line.strip().split()
    if len(log_line) == 4:
        date = log_line[0][1:]
        time = log_line[1][:-1]
        return (date,time)
    elif len(log_line) == 6:
        date = log_line[0][1:]
        time = log_line[1][:-1]
        guard_id = log_line[3]
        return (date,time,guard_id)

def part1():
    with open('day4a.txt') as input:
        d = defaultdict(list)
        curr_guard = ''
        for line in input:
            sigfigs = line.strip().split()

            if len(sigfigs) == 4:
                date, time = parse(line)
                d[curr_guard].append(time)
            elif len(sigfigs) == 6:
                date, time, curr_guard = parse(line)
            else:
                print('Unknown line encountered', line)
                return

        e = defaultdict(list)
        for k,v in d.items():
            for i in range(1,len(v)+1,2):
                time_asleep = int(v[i][-2:]) - int(v[i-1][-2:])
                #print(k,int(v[i][-2:]),int(v[i-1][-2:]),time_asleep)
                e[k].append(time_asleep)

        f = [(x,sum(y)) for x,y in e.items()] #[(guard_id, total min asleep)]

        g = max(f,key=lambda x: x[1]) # (guard_id, total min asleep)

        minutes = d.get(g[0])
        h = dict((x,0) for x in range(60))
        for i in range(1,len(minutes)+1,2):
            start = minutes[i-1][-2:]
            end = minutes[i][-2:]
            for j in range(int(start),int(end)):
                h[j] += 1
                #import ipdb; ipdb.set_trace()
                #1+1

        last_most_minute = list(h.values())[::-1].index(max(h.values()))
        print(g[0], [thing[1][0] for thing in enumerate(h.items()) if thing[0] == (59 - last_most_minute)][0])


def part2():
    with open('day4a.txt') as input:
        d = defaultdict(list)
        curr_guard = ''
        for line in input:
            sigfigs = line.strip().split()

            if len(sigfigs) == 4:
                date, time = parse(line)
                d[curr_guard].append(time)
            elif len(sigfigs) == 6:
                date, time, curr_guard = parse(line)
            else:
                print('Unknown line encountered', line)
                return

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

        overall_max = set()

        for k,v in e.items():
            for thing in v:
                overall_max.add(thing)

        the_max = max(overall_max)



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
