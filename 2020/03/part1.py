#!/usr/bin/env python3


def process_content(content: str):
    lines = content.splitlines()
    y, x, num = 0, 0, 0
    while y < len(lines):
        if lines[y][x] == '#':
            num += 1
        y += 1
        x = (x + 3) % len(lines[0])
    return num


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
