#!/usr/bin/env python3


def process_content(content: str):
    flipped = set()
    for line in content.splitlines():
        x = y = 0
        while line:
            direction, line = line[0], line[1:]
            x += {'e': 1, 'w': -1}.get(direction, 0)
            if direction in 'ns':
                y += {'n': -1, 's': 1}.get(direction, 0)
                direction, line = line[0], line[1:]
                x += [{'e': 1}, {'w': -1}][y % 2].get(direction, 0)
        if (x, y) in flipped:
            flipped.remove((x, y))
        else:
            flipped.add((x, y))
    for i in range(100):
        minx, maxx = min(f[0] for f in flipped), max(f[0] for f in flipped)
        miny, maxy = min(f[1] for f in flipped), max(f[1] for f in flipped)
        newFlipped = set()
        for x in range(minx-1, maxx+2):
            for y in range(miny-1, maxy+2):
                others = sum(1
                             for dx, dy in
                             [(-1, 0), (1, 0), (0, -1), (0, 1)] +
                             [[(-1, -1), (-1, 1)], [(1, -1), (1, 1)]][y % 2]
                             if (x+dx, y+dy) in flipped)
                if (x, y) in flipped:
                    if others in (1, 2):
                        newFlipped.add((x, y))
                else:
                    if others == 2:
                        newFlipped.add((x, y))
        flipped = newFlipped
    return len(flipped)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
