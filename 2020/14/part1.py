#!/usr/bin/env python3


def process_content(content: str):
    mem = {}
    for line in content.splitlines():
        if line.startswith('mem'):
            pos, val = map(int, line.lstrip('mem[').split('] ='))
            mem[pos] = (val & mask0) | mask1
        elif line.startswith('mask'):
            mask = line.split('=')[1].strip()
            mask0 = int(mask.replace('X', '1'), 2)
            mask1 = int(mask.replace('X', '0'), 2)
    return sum(mem.values())


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
