#!/usr/bin/env python3


def sign(value):
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0


def process_content(content: str):
    m = {}
    for line in content.splitlines():
        start, end = line.split(' -> ')
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        dx, dy = sign(x2 - x1), sign(y2 - y1)
        x, y = x1, y1
        m[(x, y)] = m.get((x, y), 0) + 1
        while x != x2 or y != y2:
            x += dx
            y += dy
            m[(x, y)] = m.get((x, y), 0) + 1
    return len([v for v in m.values() if v > 1])


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
