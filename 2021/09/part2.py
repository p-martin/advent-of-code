#!/usr/bin/env python3

import math


def get_lp(hmap):
    lp = set()
    seen = set()
    for sy, line in enumerate(hmap):
        for sx, h in enumerate(line):
            if (sx, sy) not in seen:
                x, y = sx, sy
                while True:
                    if x > 0 and hmap[y][x-1] < h:
                        x -= 1
                    elif x < len(line)-1 and hmap[y][x+1] < h:
                        x += 1
                    elif y > 0 and hmap[y-1][x] < h:
                        y -= 1
                    elif y < len(hmap)-1 and hmap[y+1][x] < h:
                        y += 1
                    else:
                        break
                    h = hmap[y][x]
                    seen.add((x, y))
                if h < 9:
                    lp.add((x, y))
    return lp


def get_flood_fill_size(hmap, sx, sy):
    basin = ff = {(sx, sy)}
    while ff:
        newff = set()
        for x, y in ff:
            h = hmap[y][x]
            if x > 0 and h < hmap[y][x-1] < 9:
                newff.add((x-1, y))
            if x < len(hmap[0])-1 and h < hmap[y][x+1] < 9:
                newff.add((x+1, y))
            if y > 0 and h < hmap[y-1][x] < 9:
                newff.add((x, y-1))
            if y < len(hmap)-1 and h < hmap[y+1][x] < 9:
                newff.add((x, y+1))
        basin |= newff
        ff = newff
    return len(basin)


def process_content(content: str):
    hmap = [tuple(map(int, line))
            for line in content.splitlines()]
    lp = get_lp(hmap)
    sizes = sorted([get_flood_fill_size(hmap, x, y)
                    for x, y in lp],
                   reverse=True)
    return math.prod(sizes[:3])


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
