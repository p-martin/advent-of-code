#!/usr/bin/env python3


def process_content(content: str):
    lines = content.splitlines()
    r = 1
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        r *= move(lines, dx, dy)
    return r


def move(lines, dx, dy):
    y, x, num = 0, 0, 0
    while y < len(lines):
        if lines[y][x] == '#':
            num += 1
        y += dy
        x = (x + dx) % len(lines[0])
    return num


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
