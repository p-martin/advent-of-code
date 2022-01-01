#!/usr/bin/env python3


def apply(algo, lit, run):
    minx, maxx = min(x for x, y in lit), max(x for x, y in lit)
    miny, maxy = min(y for x, y in lit), max(y for x, y in lit)
    newlit = set()
    for y in range(miny - 1, maxy + 2):
        for x in range(minx - 1, maxx + 2):
            px9 = []
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if algo[0] == '.' or (minx <= x+dx <= maxx and miny <= y+dy <= maxy):
                        px9.append('1' if (x+dx, y+dy) in lit else '0')
                    else:
                        px9.append('1' if run % 2 == 0 else '0')
            px9val = int(''.join(px9), 2)
            if algo[px9val] == '#':
                newlit.add((x, y))
    return newlit


def process_content(content: str):
    algo, img = content.split('\n\n')
    algo = ''.join(algo.strip().splitlines())
    lit = {(x, y)
           for y, line in enumerate(img.strip().splitlines())
           for x, c in enumerate(line)
           if c == '#'}

    for i in range(2):
        lit = apply(algo, lit, i+1)

    return len(lit)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
