#!/usr/bin/env python3


def process_content(content: str):
    on = set()
    for line in content.splitlines():
        onoff, coords = line.split()
        [(x1, x2), (y1, y2), (z1, z2)] = [map(int, coord.split('=')[-1].split('..'))
                                          for coord in coords.split(',')]
        for x in range(max(x1, -50), min(x2, 50) + 1):
            for y in range(max(y1, -50), min(y2, 50) + 1):
                for z in range(max(z1, -50), min(z2, 50) + 1):
                    if onoff == 'on':
                        on.add((x, y, z))
                    else:
                        on.discard((x, y, z))

    return len(on)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
