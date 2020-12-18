#!/usr/bin/env python3


def process_content(content: str):
    g = {0: {y: {x: (c == '#')
                 for x, c in enumerate(line)}
             for y, line in enumerate(content.splitlines())}}
    for i in range(6):
        g = calc(g)
    return totalcount(g)


def calc(g):
    newg = {}
    for z in range(min(g) - 1, max(g) + 2):
        newg[z] = {}
        for y in range(min(g[0]) - 1, max(g[0]) + 2):
            newg[z][y] = {}
            for x in range(min(g[0][0]) - 1, max(g[0][0]) + 2):
                cubes = getcubes(x, y, z, g)
                try:
                    oldval = g[z][y][x]
                except KeyError:
                    oldval = False
                if oldval:
                    newg[z][y][x] = cubes in (2, 3)
                else:
                    newg[z][y][x] = cubes == 3
    return newg


def getcubes(x, y, z, g):
    r = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                tx, ty, tz = x + dx, y + dy, z + dz
                try:
                    if g[tz][ty][tx]:
                        r += 1
                except KeyError:
                    pass
    return r


def totalcount(g):
    return sum(sum(sum(line.values())
                   for line in sl.values())
               for sl in g.values())


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
