#!/usr/bin/env python3


def process_content(content: str):
    x = y = a = 0
    for line in content.splitlines():
        d, val = line.split()
        val = int(val)
        if d == 'forward':
            x += val
            y += a * val
        a += {'down': 1, 'up': -1}.get(d, 0) * val
    return x * y


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
