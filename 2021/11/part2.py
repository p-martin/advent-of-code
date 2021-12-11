#!/usr/bin/env python3


def process_content(content: str):
    octs = [list(map(int, line))
            for line in content.splitlines()]
    step = 0
    while True:
        step += 1
        newocts = [[energy + 1 for energy in line]
                   for line in octs]
        flashed = {(x, y)
                   for y, line in enumerate(newocts)
                   for x, energy in enumerate(line)
                   if energy > 9}
        ff = flashed.copy()
        while ff:
            newff = set()
            for x, y in ff:
                for dx, dy in [(-1, -1), (0, -1), (1, -1),
                               (-1, 0), (1, 0),
                               (-1, 1), (0, 1), (1, 1)]:
                    tx, ty = x + dx, y + dy
                    if 0 <= ty < len(octs) and 0 <= tx < len(octs[0]):
                        newocts[ty][tx] += 1
                        if newocts[ty][tx] > 9 and (tx, ty) not in flashed:
                            flashed.add((tx, ty))
                            newff.add((tx, ty))
            ff = newff
        if len(flashed) == len(octs) * len(octs[0]):
            return step
        for x, y in flashed:
            newocts[y][x] = 0
        octs = newocts


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
